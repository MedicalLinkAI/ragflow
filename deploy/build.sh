#!/usr/bin/env bash
# ============================================================================
# RAGflow 应用构建脚本
# ============================================================================
# 用法：deploy/build.sh <app-id> [--env dev] [--branch medlink-dev-backup]
#   <app-id>        ragflow-api | ragflow-web | ragflow-worker
#   --env <name>    加载 deploy/.env.<name>（默认 dev）
#   --branch <name> 构建前切换并更新分支（要求工作区干净）
#   --help          显示帮助信息
#
# ragflow-api 从仓库根 Dockerfile 源码构建（首次需下载 ragflow_deps 依赖镜像）。
# ragflow-web 从主镜像提取前端产物构建轻量 nginx 镜像。
# ragflow-worker 与 ragflow-api 共享镜像，无需单独构建。
#
# 退出码：0=成功  1=失败
# ============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# ---- 颜色 ------------------------------------------------------------------
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

log_info()  { echo -e "${BLUE}[INFO]${NC}  $*"; }
log_ok()    { echo -e "${GREEN}[OK]${NC}    $*"; }
log_warn()  { echo -e "${YELLOW}[WARN]${NC}  $*"; }
log_error() { echo -e "${RED}[ERROR]${NC} $*"; }

# ---- usage ------------------------------------------------------------------
usage() {
  cat <<EOF
RAGflow 应用构建脚本

用法：
  deploy/build.sh <app-id> [--env <name>] [--branch <name>] [--help]

应用 ID：
  ragflow-api       API 服务（从仓库根 Dockerfile 源码构建）
  ragflow-web       前端应用（从主镜像提取前端产物的轻量 nginx 镜像）
  ragflow-worker    Worker 服务（与 ragflow-api 共享镜像，无需单独构建）

选项：
  --env <name>       加载 deploy/.env.<name>（默认 dev）
  --branch <name>    构建前切换并更新分支（要求工作区干净）
  --help, -h         显示此帮助信息

示例：
  deploy/build.sh ragflow-api                            # 源码构建主镜像（dev 环境）
  deploy/build.sh ragflow-web --env prod                 # 构建 web（prod 环境）
  deploy/build.sh ragflow-api --branch medlink-dev       # 切到分支后源码构建

输出：
  最后一行为机器可读 JSON：
  {"app_id":"ragflow-api","image":"<name>:<tag>","status":"success"}
EOF
}

# ---- parse_args -------------------------------------------------------------
APP_ID=""
ENV="dev"
BRANCH=""

parse_args() {
  if [[ $# -eq 0 ]]; then
    usage
    exit 1
  fi

  while [[ $# -gt 0 ]]; do
    case "$1" in
      --env)
        ENV="${2:?'--env 需要一个值（如 dev, test, prod）'}"
        shift 2
        ;;
      --branch)
        BRANCH="${2:?'--branch 需要一个分支名'}"
        shift 2
        ;;
      --help|-h)
        usage
        exit 0
        ;;
      -*)
        log_error "未知选项: $1"
        echo "运行 deploy/build.sh --help 查看帮助"
        exit 1
        ;;
      *)
        if [[ -z "$APP_ID" ]]; then
          APP_ID="$1"
        else
          log_error "多余的参数: $1"
          echo "运行 deploy/build.sh --help 查看帮助"
          exit 1
        fi
        shift
        ;;
    esac
  done

  case "${APP_ID:-}" in
    ragflow-api|ragflow-web|ragflow-worker) ;;
    *)
      log_error "无效的 app-id: ${APP_ID:-<empty>}"
      echo "有效值: ragflow-api, ragflow-web, ragflow-worker"
      echo "运行 deploy/build.sh --help 查看帮助"
      exit 1
      ;;
  esac
}

# ---- check_prerequisites ----------------------------------------------------
check_prerequisites() {
  log_info "检查前置依赖..."

  if ! command -v docker &>/dev/null; then
    log_error "Docker 未安装或不在 PATH 中"
    exit 1
  fi

  if ! docker info &>/dev/null; then
    log_error "Docker 守护进程未运行，请先启动 Docker"
    exit 1
  fi

  if ! docker compose version &>/dev/null; then
    log_error "Docker Compose V2 不可用，请升级到 Docker Compose plugin"
    exit 1
  fi

  log_ok "前置依赖检查通过"
}

# ---- load_env ---------------------------------------------------------------
COMPOSE_PROJECT_NAME=""
RAGFLOW_IMAGE=""
RAGFLOW_WEB_IMAGE=""
NEED_MIRROR="0"

load_env() {
  local env_file="$SCRIPT_DIR/.env.${ENV}"

  if [[ ! -f "$env_file" ]]; then
    log_error "环境文件不存在: $env_file"
    log_error "请从模板复制：cp deploy/.env.example deploy/.env.${ENV}"
    exit 1
  fi

  COMPOSE_PROJECT_NAME=$(grep -E '^COMPOSE_PROJECT_NAME=' "$env_file" | head -1 | cut -d'=' -f2-)
  if [[ -z "$COMPOSE_PROJECT_NAME" ]]; then
    log_error "环境文件中未定义 COMPOSE_PROJECT_NAME"
    exit 1
  fi
  export COMPOSE_PROJECT_NAME

  RAGFLOW_IMAGE=$(grep -E '^RAGFLOW_IMAGE=' "$env_file" | head -1 | cut -d'=' -f2-)
  if [[ -z "$RAGFLOW_IMAGE" ]]; then
    log_error "环境文件中未定义 RAGFLOW_IMAGE"
    exit 1
  fi
  export RAGFLOW_IMAGE

  RAGFLOW_WEB_IMAGE=$(grep -E '^RAGFLOW_WEB_IMAGE=' "$env_file" | head -1 | cut -d'=' -f2- || true)
  RAGFLOW_WEB_IMAGE="${RAGFLOW_WEB_IMAGE:-ragflow-web:latest}"
  export RAGFLOW_WEB_IMAGE

  NEED_MIRROR=$(grep -E '^NEED_MIRROR=' "$env_file" | head -1 | cut -d'=' -f2- || echo "0")
  NEED_MIRROR="${NEED_MIRROR:-0}"

  log_ok "已加载环境: ${ENV} (COMPOSE_PROJECT_NAME=${COMPOSE_PROJECT_NAME})"
}

# ---- switch_branch ----------------------------------------------------------
switch_branch() {
  if [[ -z "$BRANCH" ]]; then
    return 0
  fi

  log_info "切换到分支: ${BRANCH}"

  if ! git -C "$REPO_ROOT" diff --quiet 2>/dev/null \
     || ! git -C "$REPO_ROOT" diff --cached --quiet 2>/dev/null; then
    log_error "工作区存在未提交的变更，请先提交或暂存"
    log_error "运行 'git status' 查看详情"
    exit 1
  fi

  git -C "$REPO_ROOT" fetch origin
  git -C "$REPO_ROOT" checkout "$BRANCH"
  git -C "$REPO_ROOT" pull origin "$BRANCH"
  log_ok "已切换到分支: ${BRANCH}"
}

# ---- verify_template --------------------------------------------------------
verify_template() {
  local template="$SCRIPT_DIR/service_conf.yaml.template"

  if [[ ! -f "$template" ]]; then
    log_error "service_conf.yaml.template 不存在: $template"
    log_error "RAGflow entrypoint.sh 需要此模板文件进行配置渲染"
    exit 1
  fi

  log_ok "service_conf.yaml.template 已验证"
}

# ---- build_api (source build from Dockerfile) --------------------------------
build_api() {
  log_info "从源码构建 RAGflow 主镜像（首次构建需下载依赖，可能较慢）..."
  log_info "镜像标签: ${RAGFLOW_IMAGE}"

  log_info "开始构建镜像: ragflow-api..."
  docker build     -f "$REPO_ROOT/Dockerfile"     -t "$RAGFLOW_IMAGE"     --build-arg NEED_MIRROR="$NEED_MIRROR"     "$REPO_ROOT"
  log_ok "镜像构建完成: ${RAGFLOW_IMAGE}"
}

# ---- build_web (docker compose build) ----------------------------------------
build_web() {
  if ! docker image inspect "${RAGFLOW_IMAGE}" &>/dev/null; then
    log_error "RAGFLOW_IMAGE 不存在本地: ${RAGFLOW_IMAGE}"
    log_error "ragflow-web 构建依赖此镜像（Dockerfile.web 的 FROM 指令）"
    log_error "请先运行: deploy/build.sh ragflow-api --env ${ENV}"
    exit 1
  fi
  log_ok "基础镜像就绪: ${RAGFLOW_IMAGE}"

  log_info "构建镜像: ragflow-web（从主镜像提取前端产物 + nginx）..."
  docker build     -f "$SCRIPT_DIR/Dockerfile.web"     -t "$RAGFLOW_WEB_IMAGE"     --build-arg RAGFLOW_IMAGE="$RAGFLOW_IMAGE"     "$SCRIPT_DIR"
  log_ok "镜像构建完成"
}

# ---- tag_image --------------------------------------------------------------
IMAGE_TAG=""
IMAGE_NAME=""

tag_image() {
  IMAGE_TAG=$(date +%Y%m%d-%H%M%S)

  case "$APP_ID" in
    ragflow-api)
      IMAGE_NAME="${RAGFLOW_IMAGE%%:*}"
      docker tag "${RAGFLOW_IMAGE}" "${IMAGE_NAME}:${IMAGE_TAG}"
      log_ok "镜像已标记: ${IMAGE_NAME}:${IMAGE_TAG}"
      ;;
    ragflow-web)
      IMAGE_NAME="${RAGFLOW_WEB_IMAGE%%:*}"
      docker tag "${RAGFLOW_WEB_IMAGE}" "${IMAGE_NAME}:${IMAGE_TAG}"
      log_ok "镜像已标记: ${IMAGE_NAME}:${IMAGE_TAG}"
      ;;
  esac
}

# ---- output_result ----------------------------------------------------------
output_result() {
  echo ""
  log_ok "✅ 构建成功"

  case "$APP_ID" in
    ragflow-api)
      log_info "镜像: ${RAGFLOW_IMAGE}"
      log_info "标签: ${IMAGE_NAME}:${IMAGE_TAG}"
      echo ""
      echo "{\"app_id\":\"${APP_ID}\",\"image\":\"${IMAGE_NAME}:${IMAGE_TAG}\",\"status\":\"success\"}"
      ;;
    ragflow-web)
      log_info "镜像: ${IMAGE_NAME}:latest"
      log_info "标签: ${IMAGE_NAME}:${IMAGE_TAG}"
      echo ""
      echo "{\"app_id\":\"${APP_ID}\",\"image\":\"${IMAGE_NAME}:${IMAGE_TAG}\",\"status\":\"success\"}"
      ;;
  esac
}

# ---- main -------------------------------------------------------------------
main() {
  echo ""
  echo "=========================================="
  echo "  RAGflow 应用构建"
  echo "=========================================="
  echo ""

  parse_args "$@"
  check_prerequisites
  load_env
  switch_branch

  case "$APP_ID" in
    ragflow-worker)
      log_info "ragflow-worker 与 ragflow-api 共享镜像（${RAGFLOW_IMAGE}）"
      log_info "无需单独构建，请运行: deploy/build.sh ragflow-api --env ${ENV}"
      echo ""
      echo "{\"app_id\":\"ragflow-worker\",\"image\":\"shared-with-ragflow-api\",\"status\":\"skipped\"}"
      exit 0
      ;;
    ragflow-api)
      verify_template
      build_api
      tag_image
      output_result
      ;;
    ragflow-web)
      build_web
      tag_image
      output_result
      ;;
  esac
}

main "$@"
