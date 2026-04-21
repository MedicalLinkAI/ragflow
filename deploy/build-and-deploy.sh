#!/usr/bin/env bash
# ============================================================================
# RAGflow 构建并部署脚本
# ============================================================================
# 用法：deploy/build-and-deploy.sh <app-id> [--env dev] [--branch medlink-dev-backup]
#   <app-id>        ragflow-api | ragflow-web | ragflow-worker | ragflow-all
#   --env <name>    加载 deploy/.env.<name>（默认 dev）
#   --branch <name> 构建前切换并更新分支（要求工作区干净）
#   --help          显示帮助信息
#
# 说明：
#   - 这是 build.sh + deploy.sh 的聚合封装，不替代原脚本
#   - 适用于“代码已修改，需要重新构建镜像并发布”的常见路径
#   - 若只想基于当前镜像拉起 / 对账服务，请直接使用 deploy.sh
#
# 退出码：0=成功  1=失败
# ============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

RED='[0;31m'
GREEN='[0;32m'
YELLOW='[1;33m'
BLUE='[0;34m'
NC='[0m'

log_info()  { echo -e "${BLUE}[INFO]${NC}  $*"; }
log_ok()    { echo -e "${GREEN}[OK]${NC}    $*"; }
log_warn()  { echo -e "${YELLOW}[WARN]${NC}  $*"; }
log_error() { echo -e "${RED}[ERROR]${NC} $*"; }

usage() {
  cat <<EOF
RAGflow 构建并部署脚本

用法：
  deploy/build-and-deploy.sh <app-id> [--env <name>] [--branch <name>] [--help]

应用 ID：
  ragflow-api       构建 API 主镜像后部署 API
  ragflow-web       构建 Web 镜像后部署 Web
  ragflow-worker    复用 API 主镜像（build 阶段为 skipped）后部署 Worker
  ragflow-all       依次构建 ragflow-api / ragflow-web，然后部署全部应用

选项：
  --env <name>       加载 deploy/.env.<name>（默认 dev）
  --branch <name>    构建前切换并更新分支（要求工作区干净）
  --help, -h         显示此帮助信息

输出：
  最后一行为机器可读 JSON：
  {"app_id":"ragflow-api","action":"build-and-deploy","status":"success"}
EOF
}

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
        echo "运行 deploy/build-and-deploy.sh --help 查看帮助"
        exit 1
        ;;
      *)
        if [[ -z "$APP_ID" ]]; then
          APP_ID="$1"
        else
          log_error "多余的参数: $1"
          echo "运行 deploy/build-and-deploy.sh --help 查看帮助"
          exit 1
        fi
        shift
        ;;
    esac
  done

  case "${APP_ID:-}" in
    ragflow-api|ragflow-web|ragflow-worker|ragflow-all) ;;
    *)
      log_error "无效的 app-id: ${APP_ID:-<empty>}"
      echo "有效值: ragflow-api, ragflow-web, ragflow-worker, ragflow-all"
      echo "运行 deploy/build-and-deploy.sh --help 查看帮助"
      exit 1
      ;;
  esac
}

run_build() {
  local target="$1"
  local build_cmd=("$SCRIPT_DIR/build.sh" "$target" --env "$ENV")

  if [[ -n "$BRANCH" ]]; then
    build_cmd+=(--branch "$BRANCH")
  fi

  log_info "执行构建阶段: ${target}"
  "${build_cmd[@]}"
}

run_build_phase() {
  case "$APP_ID" in
    ragflow-all)
      run_build "ragflow-api"
      run_build "ragflow-web"
      ;;
    *)
      run_build "$APP_ID"
      ;;
  esac
}

run_deploy_phase() {
  log_info "执行部署阶段: ${APP_ID}"
  "$SCRIPT_DIR/deploy.sh" "$APP_ID" --env "$ENV"
}

output_result() {
  echo ""
  log_ok "✅ 构建并部署成功"
  echo "{\"app_id\":\"${APP_ID}\",\"action\":\"build-and-deploy\",\"status\":\"success\"}"
}

main() {
  echo ""
  echo "=========================================="
  echo "  RAGflow 构建并部署"
  echo "=========================================="
  echo ""

  parse_args "$@"
  run_build_phase
  run_deploy_phase
  output_result
}

main "$@"
