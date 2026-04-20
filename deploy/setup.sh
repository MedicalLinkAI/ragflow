#!/usr/bin/env bash
# ============================================================================
# RAGflow 基础设施初始化脚本（幂等）
# ============================================================================
# 用法：deploy/setup.sh [--env <name>] [--help]
#   --env <name>  加载 deploy/.env.<name>（默认 dev）
#   --help        显示帮助信息
#
# 基础设施组件（infra profile）：
#   - Elasticsearch 8.x（全文检索引擎）
#   - PostgreSQL + pgvector（关系数据库）
#   - Redis / Valkey（缓存与队列）
#   - MinIO（对象存储）
#
# Bootstrap 4-State 退出码：
#   0 — initialized / skipped-existing
#   1 — failed（关键故障）
#   2 — repair-required（部分健康）
# ============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# ---- 颜色 ------------------------------------------------------------------
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

log_info()  { echo -e "${BLUE}[INFO]${NC}  $*"; }
log_ok()    { echo -e "${GREEN}[OK]${NC}    $*"; }
log_warn()  { echo -e "${YELLOW}[WARN]${NC}  $*"; }
log_error() { echo -e "${RED}[ERROR]${NC} $*"; }

# ---- parse_args -------------------------------------------------------------
ENV="dev"

parse_args() {
  while [[ $# -gt 0 ]]; do
    case "$1" in
      --env)
        ENV="${2:?'--env requires a value (e.g. dev, test, prod)'}"
        shift 2
        ;;
      --help|-h)
        cat <<EOF
RAGflow 基础设施初始化脚本（幂等）

用法：
  deploy/setup.sh [--env <name>] [--help]

选项：
  --env <name>   加载 deploy/.env.<name>（默认 dev）
  --help, -h     显示此帮助信息

基础设施组件（infra profile）：
  elasticsearch   Elasticsearch 8.x（全文检索引擎）
  postgres        PostgreSQL + pgvector（关系数据库）
  redis           Redis / Valkey（缓存与队列）
  minio           MinIO（对象存储）

环境文件：
  deploy/.env.dev      开发环境（默认）
  deploy/.env.test     测试环境
  deploy/.env.prod     生产环境

示例：
  deploy/setup.sh                  # 使用 dev 环境
  deploy/setup.sh --env prod       # 使用 prod 环境

Bootstrap 状态：
  initialized       首次初始化成功（exit 0）
  skipped-existing  检测到已有数据，基础设施启动成功（exit 0）
  repair-required   部分容器不健康（exit 2）
  failed            关键故障，容器未启动（exit 1）
EOF
        exit 0
        ;;
      *)
        log_error "未知参数: $1"
        echo "运行 deploy/setup.sh --help 查看帮助"
        exit 1
        ;;
    esac
  done
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

  if docker compose version &>/dev/null; then
    log_ok "Docker Compose (plugin) 可用"
  elif command -v docker-compose &>/dev/null; then
    log_error "检测到旧版 docker-compose，请升级到 Docker Compose V2 (plugin)"
    exit 1
  else
    log_error "Docker Compose 不可用"
    exit 1
  fi

  log_ok "前置依赖检查通过"
}

# ---- load_env ---------------------------------------------------------------
COMPOSE_PROJECT_NAME=""
DATA_ROOT=""

load_env() {
  local env_file="$SCRIPT_DIR/.env.${ENV}"

  if [[ ! -f "$env_file" ]]; then
    log_error "环境文件不存在: $env_file"
    log_error "请从模板复制：cp deploy/.env.example deploy/.env.${ENV}"
    exit 1
  fi

  # 提取 COMPOSE_PROJECT_NAME（不 source 整个文件，避免副作用）
  COMPOSE_PROJECT_NAME=$(grep -E '^COMPOSE_PROJECT_NAME=' "$env_file" | head -1 | cut -d'=' -f2-)
  if [[ -z "$COMPOSE_PROJECT_NAME" ]]; then
    log_error "环境文件中未定义 COMPOSE_PROJECT_NAME"
    exit 1
  fi
  export COMPOSE_PROJECT_NAME

  # 提取 DATA_ROOT（默认 ./data）
  DATA_ROOT=$(grep -E '^DATA_ROOT=' "$env_file" | head -1 | cut -d'=' -f2-)
  DATA_ROOT="${DATA_ROOT:-./data}"
  # 相对路径基于 SCRIPT_DIR 解析
  if [[ "$DATA_ROOT" != /* ]]; then
    DATA_ROOT="$SCRIPT_DIR/$DATA_ROOT"
  fi

  log_ok "已加载环境: ${ENV} (COMPOSE_PROJECT_NAME=${COMPOSE_PROJECT_NAME}, DATA_ROOT=${DATA_ROOT})"
}

# ---- create_network ---------------------------------------------------------
create_network() {
  log_info "确保 Docker 网络 medlinkai-shared 存在..."
  docker network create medlinkai-shared 2>/dev/null || true
  log_ok "网络 medlinkai-shared 就绪"
}

# ---- detect_existing --------------------------------------------------------
FIRST_INIT=true

detect_existing() {
  if [[ -d "$DATA_ROOT/esdata" ]] && [[ -d "$DATA_ROOT/pgdata" ]]; then
    FIRST_INIT=false
    log_info "检测到已有数据目录: ${DATA_ROOT}（非首次初始化）"
  else
    FIRST_INIT=true
    log_info "未检测到完整数据目录（首次初始化）"
  fi
}

# ---- prepare_data_dirs ------------------------------------------------------
prepare_data_dirs() {
  log_info "创建数据目录..."

  local dirs=("esdata" "pgdata" "redisdata" "miniodata")
  for d in "${dirs[@]}"; do
    mkdir -p "$DATA_ROOT/$d"
  done
  log_ok "数据目录就绪: ${dirs[*]}"

  # ES 数据目录需要 UID 1000 所有权（容器内 elasticsearch 用户）
  log_info "设置 Elasticsearch 数据目录权限 (UID 1000)..."
  if [[ "$(uname -s)" == "Darwin" ]]; then
    # macOS: Docker Desktop 自动处理文件权限映射，无需 chown
    log_ok "macOS 检测到，Docker Desktop 处理文件权限，跳过 chown"
  else
    if chown -R 1000:1000 "$DATA_ROOT/esdata" 2>/dev/null; then
      log_ok "esdata 权限设置完成 (1000:1000)"
    else
      log_warn "无法设置 esdata 权限（需要 root 权限）"
      log_warn "请手动执行: sudo chown -R 1000:1000 ${DATA_ROOT}/esdata"
    fi
  fi
}

# ---- start_infra ------------------------------------------------------------
start_infra() {
  log_info "启动基础设施容器 (profile: infra)..."
  docker compose \
    -f "$SCRIPT_DIR/docker-compose.yml" \
    --env-file "$SCRIPT_DIR/.env.${ENV}" \
    --profile infra \
    up -d

  log_ok "docker compose up -d 完成"
}

# ---- wait_healthy -----------------------------------------------------------
HEALTHY_COMPONENTS=()
UNHEALTHY_COMPONENTS=()

# 4 infra containers to check
INFRA_COMPONENTS=("elasticsearch" "postgres" "redis" "minio")

wait_healthy() {
  local timeout=180
  local interval=5
  local elapsed=0
  local all_healthy=false

  log_info "等待基础设施容器健康（超时 ${timeout}s, 共 ${#INFRA_COMPONENTS[@]} 个组件）..."

  # Track per-component health
  declare -A comp_status
  for comp in "${INFRA_COMPONENTS[@]}"; do
    comp_status[$comp]="waiting"
  done

  while [[ $elapsed -lt $timeout ]]; do
    all_healthy=true

    for comp in "${INFRA_COMPONENTS[@]}"; do
      # Skip already healthy
      if [[ "${comp_status[$comp]}" == "healthy" ]]; then
        continue
      fi

      local container_name="${COMPOSE_PROJECT_NAME}-${comp}"
      local status
      status=$(docker inspect --format='{{.State.Health.Status}}' "$container_name" 2>/dev/null || echo "not_found")

      if [[ "$status" == "healthy" ]]; then
        comp_status[$comp]="healthy"
        log_ok "${comp} 健康 (${elapsed}s)"
      else
        all_healthy=false
        if [[ "$status" == "not_found" ]]; then
          log_warn "容器 ${container_name} 不存在（${elapsed}s）"
        fi
      fi
    done

    if [[ "$all_healthy" == true ]]; then
      log_ok "全部 ${#INFRA_COMPONENTS[@]} 个组件健康"
      break
    fi

    # Progress summary (not every tick — every 30s)
    if (( elapsed > 0 && elapsed % 30 == 0 )); then
      local pending=()
      for comp in "${INFRA_COMPONENTS[@]}"; do
        [[ "${comp_status[$comp]}" != "healthy" ]] && pending+=("$comp")
      done
      log_info "等待中 (${elapsed}s/${timeout}s)... 未就绪: ${pending[*]}"
    fi

    sleep "$interval"
    elapsed=$((elapsed + interval))
  done

  # Classify final state
  for comp in "${INFRA_COMPONENTS[@]}"; do
    if [[ "${comp_status[$comp]}" == "healthy" ]]; then
      HEALTHY_COMPONENTS+=("$comp")
    else
      # Final check after timeout
      local container_name="${COMPOSE_PROJECT_NAME}-${comp}"
      local final_status
      final_status=$(docker inspect --format='{{.State.Health.Status}}' "$container_name" 2>/dev/null || echo "not_found")

      if [[ "$final_status" == "healthy" ]]; then
        HEALTHY_COMPONENTS+=("$comp")
      else
        UNHEALTHY_COMPONENTS+=("$comp")
        log_warn "${comp} 在 ${timeout}s 后仍未健康 (状态: ${final_status})"
      fi
    fi
  done
}

# ---- output_status ----------------------------------------------------------
output_status() {
  local timestamp
  timestamp=$(date +%Y-%m-%dT%H:%M:%S%z)
  # 格式化时区为 +08:00 形式
  if [[ ${#timestamp} -ge 24 ]]; then
    timestamp="${timestamp:0:22}:${timestamp:22}"
  fi

  local status exit_code

  if [[ ${#UNHEALTHY_COMPONENTS[@]} -gt 0 && ${#HEALTHY_COMPONENTS[@]} -gt 0 ]]; then
    status="repair-required"
    exit_code=2
  elif [[ ${#UNHEALTHY_COMPONENTS[@]} -gt 0 ]]; then
    status="failed"
    exit_code=1
  elif [[ "$FIRST_INIT" == true ]]; then
    status="initialized"
    exit_code=0
  else
    status="skipped-existing"
    exit_code=0
  fi

  # 构建 components JSON
  local components="{"
  local first=true
  for comp in "${HEALTHY_COMPONENTS[@]}"; do
    [[ "$first" == true ]] || components+=","
    components+="\"${comp}\":\"healthy\""
    first=false
  done
  for comp in "${UNHEALTHY_COMPONENTS[@]}"; do
    [[ "$first" == true ]] || components+=","
    components+="\"${comp}\":\"unhealthy\""
    first=false
  done
  components+="}"

  # Human-readable summary
  echo ""
  case "$status" in
    initialized)
      log_ok "✅ 首次初始化完成"
      ;;
    skipped-existing)
      log_ok "✅ 检测到已有数据，基础设施已启动"
      ;;
    repair-required)
      log_warn "⚠️  部分容器不健康，需要修复"
      log_warn "不健康组件: ${UNHEALTHY_COMPONENTS[*]}"
      ;;
    failed)
      log_error "❌ 基础设施启动失败"
      log_error "不健康组件: ${UNHEALTHY_COMPONENTS[*]}"
      ;;
  esac

  # Machine-readable JSON status line
  echo "{\"status\":\"${status}\",\"timestamp\":\"${timestamp}\",\"components\":${components}}"

  exit "$exit_code"
}

# ---- main -------------------------------------------------------------------
main() {
  echo ""
  echo "=========================================="
  echo "  RAGflow 基础设施初始化"
  echo "=========================================="
  echo ""

  parse_args "$@"
  check_prerequisites
  load_env
  create_network
  detect_existing
  prepare_data_dirs
  start_infra
  wait_healthy
  output_status
}

main "$@"
