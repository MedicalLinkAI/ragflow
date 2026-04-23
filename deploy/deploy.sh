#!/usr/bin/env bash
# ============================================================================
# RAGflow 应用部署脚本
# ============================================================================
# 用法：deploy/deploy.sh <app-id> [--env dev] [--image <tag>] [--status] [--logs <app-id>]
#   <app-id>        ragflow-api | ragflow-web | ragflow-worker | ragflow-all
#   --env <name>    加载 deploy/.env.<name>（默认 dev）
#   --image <tag>   指定镜像标签（默认 latest）
#   --status        查看所有应用容器状态（无需 app-id）
#   --logs <svc>    查看指定服务日志（无需 app-id）
#   --help          显示帮助信息
#
# 退出码：0=成功（全部已部署且健康）  1=失败
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
RAGflow 应用部署脚本

用法：
  deploy/deploy.sh <app-id> [--env <name>] [--image <tag>] [--help]
  deploy/deploy.sh --status [--env <name>]
  deploy/deploy.sh --logs <service> [--env <name>]

应用 ID：
  ragflow-api       API 服务（ragflow_server + nginx）
  ragflow-web       前端应用（轻量 nginx 反向代理）
  ragflow-worker    Worker 服务（task_executor）
  ragflow-all       全部应用（按依赖顺序：api → worker → web）

选项：
  --env <name>       加载 deploy/.env.<name>（默认 dev）
  --image <tag>      指定镜像标签（默认 latest）
                     ragflow-api/worker: 覆盖 RAGFLOW_IMAGE（完整镜像引用）
                     ragflow-web: 指定构建标签（如 20250720-160000）
  --status           查看所有应用容器状态（JSON 输出）
  --logs <service>   查看指定服务日志（实时流式）
  --help, -h         显示此帮助信息

示例：
  deploy/deploy.sh ragflow-api                                      # 部署 api
  deploy/deploy.sh ragflow-all --env prod                           # 部署全部
  deploy/deploy.sh ragflow-web --image 20250720-160000              # 指定 web 镜像
  deploy/deploy.sh ragflow-api --image registry.example/ragflow:v1  # 覆盖主镜像
  deploy/deploy.sh --status                                         # 查看状态
  deploy/deploy.sh --logs ragflow-worker                            # 查看日志
EOF
}

# ---- parse_args -------------------------------------------------------------
APP_ID=""
ENV="dev"
IMAGE_TAG=""
MODE="deploy"          # deploy | status | logs
LOGS_SERVICE=""

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
      --image)
        IMAGE_TAG="${2:?'--image 需要一个镜像标签'}"
        shift 2
        ;;
      --status)
        MODE="status"
        shift
        ;;
      --logs)
        MODE="logs"
        LOGS_SERVICE="${2:?'--logs 需要一个服务名（如 ragflow-api）'}"
        shift 2
        ;;
      --help|-h)
        usage
        exit 0
        ;;
      -*)
        log_error "未知选项: $1"
        echo "运行 deploy/deploy.sh --help 查看帮助"
        exit 1
        ;;
      *)
        if [[ -z "$APP_ID" ]]; then
          APP_ID="$1"
        else
          log_error "多余的参数: $1"
          echo "运行 deploy/deploy.sh --help 查看帮助"
          exit 1
        fi
        shift
        ;;
    esac
  done

  # --status and --logs don't require app-id
  if [[ "$MODE" == "status" || "$MODE" == "logs" ]]; then
    return 0
  fi

  # Deploy mode requires valid app-id
  case "${APP_ID:-}" in
    ragflow-api|ragflow-web|ragflow-worker|ragflow-all) ;;
    *)
      log_error "无效的 app-id: ${APP_ID:-<empty>}"
      echo "有效值: ragflow-api, ragflow-web, ragflow-worker, ragflow-all"
      echo "运行 deploy/deploy.sh --help 查看帮助"
      exit 1
      ;;
  esac

  # --image is ambiguous with ragflow-all
  if [[ "$APP_ID" == "ragflow-all" && -n "$IMAGE_TAG" ]]; then
    log_error "--image 不能与 ragflow-all 一起使用（无法确定目标应用）"
    exit 1
  fi
}

# ---- load_env ---------------------------------------------------------------
COMPOSE_PROJECT_NAME=""
RAGFLOW_IMAGE=""
RAGFLOW_WEB_IMAGE=""
RAGFLOW_API_HOST_PORT=""
RAGFLOW_WEB_HOST_PORT=""
POSTGRES_USER=""
POSTGRES_DBNAME=""
SYNC_CALLBACK_URL=""
STATE_FILE=""
BASE_SQL_FILE=""

read_env_value() {
  local env_file="$1"
  local key="$2"

  python3 - "$env_file" "$key" <<'PY2'
import sys
from pathlib import Path

env_path = Path(sys.argv[1])
key = sys.argv[2]
for raw_line in env_path.read_text().splitlines():
    line = raw_line.strip()
    if not line or line.startswith('#') or '=' not in line:
        continue
    name, value = line.split('=', 1)
    if name != key:
        continue
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        value = value[1:-1]
    print(value)
    raise SystemExit(0)
raise SystemExit(1)
PY2
}

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

  RAGFLOW_API_HOST_PORT=$(grep -E '^RAGFLOW_API_HOST_PORT=' "$env_file" | head -1 | cut -d'=' -f2- || echo "19380")
  RAGFLOW_WEB_HOST_PORT=$(grep -E '^RAGFLOW_WEB_HOST_PORT=' "$env_file" | head -1 | cut -d'=' -f2- || echo "18080")
  RAGFLOW_API_HOST_PORT="${RAGFLOW_API_HOST_PORT:-19380}"
  RAGFLOW_WEB_HOST_PORT="${RAGFLOW_WEB_HOST_PORT:-18080}"
  if ! POSTGRES_USER="$(read_env_value "$env_file" POSTGRES_USER)"; then
    POSTGRES_USER=""
  fi
  if ! POSTGRES_DBNAME="$(read_env_value "$env_file" POSTGRES_DBNAME)"; then
    POSTGRES_DBNAME=""
  fi
  if ! SYNC_CALLBACK_URL="$(read_env_value "$env_file" SYNC_CALLBACK_URL)"; then
    SYNC_CALLBACK_URL=""
  fi
  STATE_FILE="$SCRIPT_DIR/.state/infra.${ENV}.json"
  BASE_SQL_FILE="$SCRIPT_DIR/sql/base.sql"

  if [[ -z "$POSTGRES_USER" || -z "$POSTGRES_DBNAME" || -z "$SYNC_CALLBACK_URL" ]]; then
    log_error "环境文件中未定义 POSTGRES_USER、POSTGRES_DBNAME 或 SYNC_CALLBACK_URL"
    exit 1
  fi

  log_ok "已加载环境: ${ENV} (COMPOSE_PROJECT_NAME=${COMPOSE_PROJECT_NAME})"
}

# ---- compose helper ---------------------------------------------------------
COMPOSE_CMD=""

setup_compose_cmd() {
  COMPOSE_CMD="docker compose -f $SCRIPT_DIR/docker-compose.yml --env-file $SCRIPT_DIR/.env.${ENV}"
}

read_state_field() {
  local field="$1"

  python3 - "$STATE_FILE" "$field" <<'PY2'
import json
import sys
from pathlib import Path

state_path = Path(sys.argv[1])
field = sys.argv[2]
if not state_path.exists():
    raise SystemExit(0)
with state_path.open() as fh:
    data = json.load(fh)
value = data.get(field, "")
if isinstance(value, bool):
    print(str(value).lower())
    raise SystemExit(0)
if value is None:
    value = ""
print(value)
PY2
}

update_base_sql_state() {
  local applied="$1"
  local pending="$2"

  python3 - "$STATE_FILE" "$applied" "$pending" <<'PY2'
import json
import sys
from pathlib import Path

state_path = Path(sys.argv[1])
data = json.loads(state_path.read_text()) if state_path.exists() and state_path.stat().st_size > 0 else {}
data["base_sql_file"] = "deploy/sql/base.sql"
data["base_sql_applied"] = sys.argv[2] == "true"
data["base_sql_pending"] = sys.argv[3] == "true"
state_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
PY2
}

database_has_base_sql_data() {
  local container_name="$1"

  docker exec "$container_name"     psql -U "$POSTGRES_USER" -d "$POSTGRES_DBNAME" -tAc     'SELECT EXISTS (SELECT 1 FROM "knowledgebase" LIMIT 1);'     2>/dev/null | tr -d '[:space:]'
}

render_base_sql_file() {
  local rendered_file

  mkdir -p "$SCRIPT_DIR/.state"
  rendered_file="$(mktemp "$SCRIPT_DIR/.state/base.sql.${ENV}.XXXXXX.sql")"
  python3 - "$BASE_SQL_FILE" "$rendered_file" "$SYNC_CALLBACK_URL" <<'PY2'
from pathlib import Path
import sys

base_sql = Path(sys.argv[1]).read_text()
rendered_path = Path(sys.argv[2])
callback_url = sys.argv[3]
placeholder = "${SYNC_CALLBACK_URL}"
if placeholder not in base_sql:
    raise SystemExit("base.sql missing ${SYNC_CALLBACK_URL} placeholder")
rendered_path.write_text(base_sql.replace(placeholder, callback_url))
PY2
  printf '%s
' "$rendered_file"
}

run_base_sql_if_needed() {
  local base_sql_pending base_sql_applied container_name data_exists rendered_base_sql

  container_name="$COMPOSE_PROJECT_NAME-postgres"
  data_exists="$(database_has_base_sql_data "$container_name" || true)"

  if [[ ! -e "$STATE_FILE" || ! -s "$STATE_FILE" ]]; then
    if [[ "$data_exists" == "t" || "$data_exists" == "true" ]]; then
      log_error "检测到数据库中已存在基础 SQL 哨兵数据，但状态文件缺失或为空: $STATE_FILE"
      log_error "为避免回写不完整的 infra 状态，已停止应用部署；请先执行 deploy/setup.sh --env ${ENV} 恢复完整状态，再重新执行当前 deploy.sh 命令"
      echo ""
      echo '{"app_id":"ragflow-api","status":"failed","reason":"base_sql_state_recovery_required"}'
      exit 1
    fi
    log_error "未检测到基础 SQL 状态文件，且数据库中不存在基础 SQL 哨兵数据: $STATE_FILE"
    echo ""
    echo '{"app_id":"ragflow-api","status":"failed","reason":"base_sql_state_missing"}'
    exit 1
  fi

  if ! base_sql_pending="$(read_state_field base_sql_pending)"; then
    log_error "基础 SQL 状态读取失败: $STATE_FILE"
    echo ""
    echo '{"app_id":"ragflow-api","status":"failed","reason":"base_sql_state_invalid"}'
    exit 1
  fi

  if ! base_sql_applied="$(read_state_field base_sql_applied)"; then
    log_error "基础 SQL 状态读取失败: $STATE_FILE"
    echo ""
    echo '{"app_id":"ragflow-api","status":"failed","reason":"base_sql_state_invalid"}'
    exit 1
  fi

  if [[ "$base_sql_applied" == "true" ]]; then
    log_ok "基础 SQL 已初始化，跳过再次执行"
    return 0
  fi

  if [[ "$data_exists" == "t" || "$data_exists" == "true" ]]; then
    update_base_sql_state true false
    log_ok "检测到基础 SQL 哨兵数据已存在，按已初始化处理"
    return 0
  fi

  if [[ "$base_sql_pending" != "true" && "$base_sql_applied" != "false" ]]; then
    log_error "未检测到待执行基础 SQL 标记，且数据库中不存在基础 SQL 哨兵数据"
    echo ""
    echo '{"app_id":"ragflow-api","status":"failed","reason":"base_sql_state_missing"}'
    exit 1
  fi

  if [[ ! -f "$BASE_SQL_FILE" ]]; then
    log_error "基础 SQL 文件不存在: $BASE_SQL_FILE"
    echo ""
    echo '{"app_id":"ragflow-api","status":"failed","reason":"base_sql_missing"}'
    exit 1
  fi

  rendered_base_sql="$(render_base_sql_file)"

  log_info "导入基础 SQL: $BASE_SQL_FILE"
  if ! docker exec -i "$container_name" psql -v ON_ERROR_STOP=1 -U "$POSTGRES_USER" -d "$POSTGRES_DBNAME" < "$rendered_base_sql"; then
    rm -f "$rendered_base_sql"
    echo ""
    echo '{"app_id":"ragflow-api","status":"failed","reason":"base_sql_import_failed"}'
    exit 1
  fi
  rm -f "$rendered_base_sql"

  update_base_sql_state true false
  log_ok "已记录基础 SQL 初始化完成: $STATE_FILE"
}

# ---- infra_preflight --------------------------------------------------------
infra_preflight() {
  log_info "检查基础设施服务..."

  local infra_names=("elasticsearch" "postgres" "redis" "minio")
  local all_running=true

  for svc in "${infra_names[@]}"; do
    local container="${COMPOSE_PROJECT_NAME}-${svc}"

    if ! docker inspect --format='{{.State.Running}}' "$container" 2>/dev/null | grep -q "true"; then
      log_error "基础设施容器未运行: ${container}"
      all_running=false
      continue
    fi

    local health
    health=$(docker inspect --format='{{if .State.Health}}{{.State.Health.Status}}{{else}}running{{end}}' \
      "$container" 2>/dev/null || echo "unknown")

    if [[ "$health" == "healthy" || "$health" == "running" ]]; then
      log_ok "${container}: ${health}"
    else
      log_warn "${container}: ${health}（非 healthy）"
    fi
  done

  if [[ "$all_running" == "false" ]]; then
    log_error "⚠️  基础设施未就绪，请先运行: deploy/setup.sh --env ${ENV}"
    exit 1
  fi

  log_ok "基础设施就绪"
}

# ---- retag_image ------------------------------------------------------------
retag_image() {
  if [[ -z "$IMAGE_TAG" ]]; then
    return 0
  fi

  case "$APP_ID" in
    ragflow-api|ragflow-worker)
      # Override RAGFLOW_IMAGE — compose reads this from environment
      log_info "覆盖 RAGFLOW_IMAGE: ${IMAGE_TAG}"
      export RAGFLOW_IMAGE="${IMAGE_TAG}"
      log_ok "RAGFLOW_IMAGE 已设置为: ${IMAGE_TAG}"
      ;;
    ragflow-web)
      local web_repo="${RAGFLOW_WEB_IMAGE%%:*}"
      if ! docker image inspect "${web_repo}:${IMAGE_TAG}" &>/dev/null; then
        log_error "镜像不存在: ${web_repo}:${IMAGE_TAG}"
        log_error "请先运行 deploy/build.sh ragflow-web 构建镜像"
        exit 1
      fi
      log_info "切换镜像: ${web_repo}:${IMAGE_TAG} → ${RAGFLOW_WEB_IMAGE}"
      docker tag "${web_repo}:${IMAGE_TAG}" "${RAGFLOW_WEB_IMAGE}"
      log_ok "镜像标签已更新"
      ;;
  esac
}

# ---- deploy_service ---------------------------------------------------------
deploy_service() {
  local service="$1"
  local profile

  case "$service" in
    ragflow-api|ragflow-web) profile="api" ;;
    ragflow-worker)          profile="worker" ;;
  esac

  log_info "部署服务: ${service} (profile: ${profile})..."
  $COMPOSE_CMD --profile infra --profile "$profile" up -d "$service"
  log_ok "容器已启动: ${service}"
}

# ---- wait_healthy -----------------------------------------------------------
wait_healthy() {
  local service="$1"
  local elapsed=0

  case "$service" in
    ragflow-api)
      local timeout=120
      local interval=5
      local health_url="http://localhost:${RAGFLOW_API_HOST_PORT}/v1/system/healthz"
      log_info "等待 ${service} 就绪 (${health_url}, 超时 ${timeout}s)..."
      while [[ $elapsed -lt $timeout ]]; do
        if curl -sf -o /dev/null --max-time 3 "$health_url" 2>/dev/null; then
          log_ok "${service} 就绪 (${elapsed}s)"
          return 0
        fi
        sleep "$interval"
        elapsed=$((elapsed + interval))
      done
      ;;
    ragflow-web)
      local timeout=60
      local interval=3
      local health_url="http://localhost:${RAGFLOW_WEB_HOST_PORT}/"
      log_info "等待 ${service} 就绪 (${health_url}, 超时 ${timeout}s)..."
      while [[ $elapsed -lt $timeout ]]; do
        if curl -sf -o /dev/null --max-time 3 "$health_url" 2>/dev/null; then
          log_ok "${service} 就绪 (${elapsed}s)"
          return 0
        fi
        sleep "$interval"
        elapsed=$((elapsed + interval))
      done
      ;;
    ragflow-worker)
      local timeout=30
      local interval=3
      local container="${COMPOSE_PROJECT_NAME}-worker"
      log_info "等待 ${service} 运行 (container: ${container}, 超时 ${timeout}s)..."
      while [[ $elapsed -lt $timeout ]]; do
        local state
        state=$(docker inspect --format='{{.State.Status}}' "$container" 2>/dev/null || echo "unknown")
        if [[ "$state" == "running" ]]; then
          log_ok "${service} 运行中 (${elapsed}s)"
          return 0
        fi
        sleep "$interval"
        elapsed=$((elapsed + interval))
      done
      ;;
  esac

  log_error "${service} 在 ${timeout}s 后仍未就绪"
  log_error "查看日志: deploy/deploy.sh --logs ${service} --env ${ENV}"
  return 1
}

# ---- get_container_json -----------------------------------------------------
get_container_json() {
  local service="$1"
  local suffix

  case "$service" in
    ragflow-api)    suffix="api" ;;
    ragflow-web)    suffix="web" ;;
    ragflow-worker) suffix="worker" ;;
  esac

  local container_name="${COMPOSE_PROJECT_NAME}-${suffix}"

  local state="stopped"
  local health="N/A"
  local ports=""

  if docker inspect "$container_name" &>/dev/null; then
    state=$(docker inspect --format='{{.State.Status}}' "$container_name" 2>/dev/null || echo "unknown")

    health=$(docker inspect --format='{{if .State.Health}}{{.State.Health.Status}}{{else}}N/A{{end}}' \
      "$container_name" 2>/dev/null || echo "N/A")

    ports=$(docker inspect --format='{{range $p, $conf := .NetworkSettings.Ports}}{{$p}}->{{range $conf}}{{.HostIp}}:{{.HostPort}}{{end}} {{end}}' \
      "$container_name" 2>/dev/null || echo "")
    ports=$(echo "$ports" | xargs)
  fi

  echo "{\"name\":\"${container_name}\",\"service\":\"${service}\",\"status\":\"${state}\",\"health\":\"${health}\",\"ports\":\"${ports}\"}"
}

# ---- handle_status ----------------------------------------------------------
handle_status() {
  log_info "查询应用容器状态..."

  local api_json web_json worker_json
  api_json=$(get_container_json "ragflow-api")
  web_json=$(get_container_json "ragflow-web")
  worker_json=$(get_container_json "ragflow-worker")

  echo ""
  echo "{\"containers\":[${api_json},${web_json},${worker_json}]}"
}

# ---- handle_logs ------------------------------------------------------------
handle_logs() {
  case "$LOGS_SERVICE" in
    ragflow-api|ragflow-web|ragflow-worker) ;;
    *)
      log_error "无效的服务名: ${LOGS_SERVICE}"
      echo "有效值: ragflow-api, ragflow-web, ragflow-worker"
      exit 1
      ;;
  esac

  local profile
  case "$LOGS_SERVICE" in
    ragflow-api|ragflow-web) profile="api" ;;
    ragflow-worker)          profile="worker" ;;
  esac

  log_info "查看日志: ${LOGS_SERVICE} (Ctrl+C 退出)..."
  $COMPOSE_CMD --profile infra --profile "$profile" logs -f "$LOGS_SERVICE"
}

# ---- deploy_and_verify ------------------------------------------------------
deploy_and_verify() {
  local service="$1"
  deploy_service "$service"

  if ! wait_healthy "$service"; then
    echo ""
    echo "{\"app_id\":\"${service}\",\"status\":\"failed\",\"reason\":\"health_timeout\"}"
    exit 1
  fi
}

# ---- output_deploy_result ---------------------------------------------------
output_deploy_result() {
  echo ""
  log_ok "✅ 部署成功"

  if [[ "$APP_ID" == "ragflow-all" ]]; then
    local api_json web_json worker_json
    api_json=$(get_container_json "ragflow-api")
    web_json=$(get_container_json "ragflow-web")
    worker_json=$(get_container_json "ragflow-worker")
    echo "{\"app_id\":\"ragflow-all\",\"status\":\"success\",\"containers\":[${api_json},${web_json},${worker_json}]}"
  else
    local container_json
    container_json=$(get_container_json "$APP_ID")
    echo "{\"app_id\":\"${APP_ID}\",\"status\":\"success\",\"containers\":[${container_json}]}"
  fi
}

# ---- main -------------------------------------------------------------------
main() {
  echo ""
  echo "=========================================="
  echo "  RAGflow 应用部署"
  echo "=========================================="
  echo ""

  parse_args "$@"
  load_env
  setup_compose_cmd

  # --- Status mode ---
  if [[ "$MODE" == "status" ]]; then
    handle_status
    exit 0
  fi

  # --- Logs mode ---
  if [[ "$MODE" == "logs" ]]; then
    handle_logs
    exit 0
  fi

  # --- Deploy mode ---
  infra_preflight

  case "$APP_ID" in
    ragflow-api)
      retag_image
      deploy_and_verify "ragflow-api"
      run_base_sql_if_needed
      ;;
    ragflow-web)
      retag_image
      deploy_and_verify "ragflow-web"
      ;;
    ragflow-worker)
      retag_image
      deploy_and_verify "ragflow-worker"
      ;;
    ragflow-all)
      deploy_and_verify "ragflow-api"
      run_base_sql_if_needed
      deploy_and_verify "ragflow-worker"
      deploy_and_verify "ragflow-web"
      ;;
  esac

  output_deploy_result
}

main "$@"
