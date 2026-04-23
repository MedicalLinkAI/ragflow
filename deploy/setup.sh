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
ES_VOLUME_NAME=""
POSTGRES_VOLUME_NAME=""
REDIS_VOLUME_NAME=""
MINIO_VOLUME_NAME=""
STORAGE_BINDING_ID=""
STATE_DIR=""
STATE_FILE=""

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

  ES_VOLUME_NAME="${COMPOSE_PROJECT_NAME}_esdata"
  POSTGRES_VOLUME_NAME="${COMPOSE_PROJECT_NAME}_pgdata"
  REDIS_VOLUME_NAME="${COMPOSE_PROJECT_NAME}_redisdata"
  MINIO_VOLUME_NAME="${COMPOSE_PROJECT_NAME}_miniodata"
  STORAGE_BINDING_ID="$(build_volume_storage_binding_id "$ES_VOLUME_NAME" "$POSTGRES_VOLUME_NAME" "$REDIS_VOLUME_NAME" "$MINIO_VOLUME_NAME")"

  STATE_DIR="$SCRIPT_DIR/.state"
  STATE_FILE="$STATE_DIR/infra.${ENV}.json"

  log_ok "已加载环境: ${ENV} (COMPOSE_PROJECT_NAME=${COMPOSE_PROJECT_NAME}, volumes=${ES_VOLUME_NAME},${POSTGRES_VOLUME_NAME},${REDIS_VOLUME_NAME},${MINIO_VOLUME_NAME})"
}

# ---- create_network ---------------------------------------------------------
create_network() {
  log_info "确保 Docker 网络 medlinkai-shared 存在..."
  docker network create medlinkai-shared 2>/dev/null || true
  log_ok "网络 medlinkai-shared 就绪"
}

normalize_path() {
  python3 - "$1" <<'PY2'
from pathlib import Path
import sys

print(Path(sys.argv[1]).resolve(strict=False))
PY2
}

build_bind_storage_binding_id() {
  local path="$1"
  echo "bind:$(normalize_path "$path")"
}

build_volume_storage_binding_id() {
  local es_volume="$1"
  local pg_volume="$2"
  local redis_volume="$3"
  local minio_volume="$4"
  echo "volumes:${es_volume},${pg_volume},${redis_volume},${minio_volume}"
}

read_container_storage_binding_id() {
  local container_name="$1"
  local destination="$2"
  local mounts_json

  mounts_json=$(docker inspect --format='{{json .Mounts}}' "$container_name" 2>/dev/null || true)
  [[ -n "$mounts_json" ]] || return 1

  python3 - "$destination" "$mounts_json" <<'PY2'
import json
import sys
from pathlib import Path

try:
    mounts = json.loads(sys.argv[2])
except json.JSONDecodeError:
    raise SystemExit(1)

destination = sys.argv[1]
for mount in mounts:
    if mount.get("Destination") != destination:
        continue
    mount_type = mount.get("Type", "")
    if mount_type == "bind":
        source = mount.get("Source", "")
        print(f"bind:{Path(source).resolve(strict=False)}")
        raise SystemExit(0)
    if mount_type == "volume":
        name = mount.get("Name", "")
        print(f"volume:{name}")
        raise SystemExit(0)
    source = mount.get("Source") or mount.get("Name") or ""
    print(f"{mount_type}:{source}")
    raise SystemExit(0)

raise SystemExit(1)
PY2
}

managed_container_specs() {
  cat <<EOF
elasticsearch|${COMPOSE_PROJECT_NAME}-elasticsearch|/usr/share/elasticsearch/data|volume:${ES_VOLUME_NAME}
postgres|${COMPOSE_PROJECT_NAME}-postgres|/var/lib/postgresql/data|volume:${POSTGRES_VOLUME_NAME}
redis|${COMPOSE_PROJECT_NAME}-redis|/data|volume:${REDIS_VOLUME_NAME}
minio|${COMPOSE_PROJECT_NAME}-minio|/data|volume:${MINIO_VOLUME_NAME}
EOF
}

validate_host_instance_conflicts() {
  local component container_name destination expected_binding actual_binding

  while IFS='|' read -r component container_name destination expected_binding; do
    [[ -n "$container_name" ]] || continue

    if ! docker inspect "$container_name" >/dev/null 2>&1; then
      continue
    fi

    if ! actual_binding="$(read_container_storage_binding_id "$container_name" "$destination")"; then
      log_error "检测到宿主机上已有容器 ${container_name}，但无法识别其挂载到 ${destination} 的存储绑定"
      log_error "为避免把同一套实例切到另一套存储，已终止部署；请先检查该容器的挂载配置"
      exit 1
    fi

    if [[ "$actual_binding" != "$expected_binding" ]]; then
      log_error "检测到宿主机级实例冲突：容器 ${container_name} 已存在，但存储绑定不一致"
      log_error "当前配置期望 ${component} 使用 ${expected_binding}，运行中容器实际使用 ${actual_binding}"
      log_error "风险：同名容器和同宿主机端口会继续复用当前实例，却切到另一套存储，导致读写目标混乱"
      log_error "处理建议：若要接管当前实例，请先停止已有实例并确认迁移；若要并行多套部署，请同时修改 COMPOSE_PROJECT_NAME、宿主机端口和内部服务引用后再重试"
      exit 1
    fi
  done < <(managed_container_specs)

  log_ok "宿主机级实例冲突校验通过"
}

ensure_state_dir() {
  mkdir -p "$STATE_DIR"
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
if value is None:
    value = ""
print(value)
PY2
}

validate_storage_binding() {
  if [[ ! -e "$STATE_FILE" ]]; then
    log_info "未检测到存储绑定记录: ${STATE_FILE}（首次部署不会拦截，待健康检查通过后写入绑定）"
    return 0
  fi

  if [[ ! -s "$STATE_FILE" ]]; then
    log_warn "检测到空的存储绑定记录: ${STATE_FILE}（按首次部署处理，不执行防重拦截）"
    return 0
  fi

  local stored_project stored_binding stored_data_root
  if ! stored_project="$(read_state_field compose_project_name)"; then
    log_error "存储绑定记录损坏，无法解析: ${STATE_FILE}"
    log_error "为避免误绑定到另一套存储，已终止部署；请检查或删除该状态文件后重试"
    exit 1
  fi

  stored_binding="$(read_state_field storage_binding_id || true)"
  if [[ -z "$stored_binding" ]]; then
    if ! stored_data_root="$(read_state_field data_root)"; then
      log_error "存储绑定记录损坏，无法解析: ${STATE_FILE}"
      log_error "为避免误绑定到另一套存储，已终止部署；请检查或删除该状态文件后重试"
      exit 1
    fi
    if [[ -n "$stored_data_root" ]]; then
      stored_binding="$(build_bind_storage_binding_id "$stored_data_root")"
    fi
  fi

  if [[ "$stored_project" != "$COMPOSE_PROJECT_NAME" ]]; then
    log_error "检测到存储绑定冲突：当前 COMPOSE_PROJECT_NAME=${COMPOSE_PROJECT_NAME}，历史绑定为 ${stored_project}"
    log_error "风险：继续执行可能会悄悄起出第二套空白 PostgreSQL/Elasticsearch/Redis/MinIO，导致误以为历史数据丢失"
    log_error "处理建议：确认是否切错了 .env / 项目名；若确实要迁移存储，请先人工确认并清理 ${STATE_FILE}"
    exit 1
  fi

  if [[ -z "$stored_binding" ]]; then
    log_error "存储绑定记录缺少 storage_binding_id/data_root: ${STATE_FILE}"
    log_error "为避免误绑定到另一套存储，已终止部署；请检查或删除该状态文件后重试"
    exit 1
  fi

  if [[ "$stored_binding" != "$STORAGE_BINDING_ID" ]]; then
    log_error "检测到存储绑定冲突：当前 storage_binding_id=${STORAGE_BINDING_ID}，历史绑定为 ${stored_binding}"
    log_error "风险：继续执行可能会绑定到另一套空目录并重新初始化存储引擎，造成历史数据被绕开"
    log_error "处理建议：确认是否切错了数据目录；若确实要迁移存储，请先人工确认并清理 ${STATE_FILE}"
    exit 1
  fi

  log_ok "存储绑定校验通过 (${COMPOSE_PROJECT_NAME} -> ${STORAGE_BINDING_ID})"
}

# ---- detect_existing --------------------------------------------------------
FIRST_INIT=true

volume_exists() {
  local volume_name="$1"
  docker volume inspect "$volume_name" >/dev/null 2>&1
}

detect_existing() {
  local volumes=("$ES_VOLUME_NAME" "$POSTGRES_VOLUME_NAME" "$REDIS_VOLUME_NAME" "$MINIO_VOLUME_NAME")
  local existing=0
  local volume_name

  for volume_name in "${volumes[@]}"; do
    if volume_exists "$volume_name"; then
      existing=$((existing + 1))
    fi
  done

  if [[ $existing -eq 0 ]]; then
    FIRST_INIT=true
    log_info "未检测到状态卷（首次初始化）"
    return 0
  fi

  if [[ $existing -eq ${#volumes[@]} ]]; then
    FIRST_INIT=false
    log_info "检测到已有状态卷（非首次初始化）: ${volumes[*]}"
    return 0
  fi

  log_error "检测到部分已存在的状态卷 (${existing}/${#volumes[@]})，拒绝继续初始化以避免混入新旧数据"
  log_error "请先检查以下卷是否完整: ${volumes[*]}"
  exit 1
}

# ---- prepare_managed_volumes -------------------------------------------------
prepare_managed_volumes() {
  log_info "使用 Docker volumes 管理状态数据..."
  log_ok "期望状态卷: ${ES_VOLUME_NAME} ${POSTGRES_VOLUME_NAME} ${REDIS_VOLUME_NAME} ${MINIO_VOLUME_NAME}"
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

array_contains() {
  local needle="$1"
  shift || true

  local item
  for item in "$@"; do
    [[ "$item" == "$needle" ]] && return 0
  done
  return 1
}

wait_healthy() {
  local timeout=180
  local interval=5
  local elapsed=0
  local all_healthy=false

  log_info "等待基础设施容器健康（超时 ${timeout}s, 共 ${#INFRA_COMPONENTS[@]} 个组件）..."

  while [[ $elapsed -lt $timeout ]]; do
    all_healthy=true
    local pending=()

    for comp in "${INFRA_COMPONENTS[@]}"; do
      if array_contains "$comp" ${HEALTHY_COMPONENTS[@]+"${HEALTHY_COMPONENTS[@]}"}; then
        continue
      fi

      local container_name="${COMPOSE_PROJECT_NAME}-${comp}"
      local status
      status=$(docker inspect --format='{{.State.Health.Status}}' "$container_name" 2>/dev/null || echo "not_found")

      if [[ "$status" == "healthy" ]]; then
        log_ok "${comp} 健康 (${elapsed}s)"
        HEALTHY_COMPONENTS+=("$comp")
      else
        all_healthy=false
        pending+=("$comp")
        if [[ "$status" == "not_found" ]]; then
          log_warn "容器 ${container_name} 不存在（${elapsed}s）"
        fi
      fi
    done

    if [[ "$all_healthy" == true ]]; then
      log_ok "全部 ${#INFRA_COMPONENTS[@]} 个组件健康"
      break
    fi

    if (( elapsed > 0 && elapsed % 30 == 0 )) && [[ ${#pending[@]} -gt 0 ]]; then
      log_info "等待中 (${elapsed}s/${timeout}s)... 未就绪: ${pending[*]}"
    fi

    sleep "$interval"
    elapsed=$((elapsed + interval))
  done

  for comp in "${INFRA_COMPONENTS[@]}"; do
    if ! array_contains "$comp" ${HEALTHY_COMPONENTS[@]+"${HEALTHY_COMPONENTS[@]}"}; then
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

persist_storage_binding_if_safe() {
  if [[ ${#HEALTHY_COMPONENTS[@]} -eq 0 || ${#UNHEALTHY_COMPONENTS[@]} -gt 0 ]]; then
    return 0
  fi

  python3 - "$STATE_FILE" "$ENV" "$COMPOSE_PROJECT_NAME" "$STORAGE_BINDING_ID" "$FIRST_INIT" "$ES_VOLUME_NAME" "$POSTGRES_VOLUME_NAME" "$REDIS_VOLUME_NAME" "$MINIO_VOLUME_NAME" <<'PY2'
import json
import sys
from pathlib import Path

state_path = Path(sys.argv[1])
state_path.parent.mkdir(parents=True, exist_ok=True)
existing = {}
if state_path.exists() and state_path.stat().st_size > 0:
    existing = json.loads(state_path.read_text())
payload = {
    "env": sys.argv[2],
    "compose_project_name": sys.argv[3],
    "storage_binding_id": sys.argv[4],
    "storage_kind": "volume",
    "volume_names": {
        "elasticsearch": sys.argv[6],
        "postgres": sys.argv[7],
        "redis": sys.argv[8],
        "minio": sys.argv[9],
    },
    "managed_components": ["elasticsearch", "postgres", "redis", "minio"],
    "base_sql_file": "deploy/sql/base.sql",
}
if "base_sql_pending" in existing:
    payload["base_sql_pending"] = existing["base_sql_pending"]
elif sys.argv[5] == "true":
    payload["base_sql_pending"] = True
if "base_sql_applied" in existing:
    payload["base_sql_applied"] = existing["base_sql_applied"]
elif sys.argv[5] == "true":
    payload["base_sql_applied"] = False
payload = {**existing, **payload}
state_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
PY2

  log_ok "已记录存储绑定: $STATE_FILE"
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
  local healthy_count unhealthy_count

  set +u
  healthy_count=${#HEALTHY_COMPONENTS[@]}
  unhealthy_count=${#UNHEALTHY_COMPONENTS[@]}
  set -u

  if [[ $unhealthy_count -gt 0 && $healthy_count -gt 0 ]]; then
    status="repair-required"
    exit_code=2
  elif [[ $unhealthy_count -gt 0 ]]; then
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
  for comp in ${HEALTHY_COMPONENTS[@]+"${HEALTHY_COMPONENTS[@]}"}; do
    [[ "$first" == true ]] || components+=","
    components+="\"${comp}\":\"healthy\""
    first=false
  done
  for comp in ${UNHEALTHY_COMPONENTS[@]+"${UNHEALTHY_COMPONENTS[@]}"}; do
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
  ensure_state_dir
  validate_storage_binding
  validate_host_instance_conflicts
  create_network
  detect_existing
  prepare_managed_volumes
  start_infra
  wait_healthy
  persist_storage_binding_if_safe
  output_status
}

main "$@"
