#!/bin/bash
# RAGFlow 基础中间件启动脚本
# 启动 docker-compose-base.yml 中的所有依赖服务
# 支持的中间件：MySQL, Elasticsearch/OpenSearch/OceanBase/Infinity, Redis, MinIO

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

mkdir -p logs

# ============================================================================
# 配置
# ============================================================================
DOC_ENGINE="${DOC_ENGINE:-elasticsearch}"
DEVICE="${DEVICE:-cpu}"
PROFILES="${DOC_ENGINE},${DEVICE}"

# ============================================================================
# 工具函数
# ============================================================================
log_info() {
    echo "ℹ️  $*"
}

log_success() {
    echo "✅ $*"
}

log_warn() {
    echo "⚠️  $*"
}

log_error() {
    echo "❌ $*"
}

# ============================================================================
# 前置检查
# ============================================================================
check_dependencies() {
    if ! command -v docker &> /dev/null; then
        log_error "Docker 未安装，请先安装 Docker"
        exit 1
    fi
    
    if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
        log_error "Docker Compose 未安装，请先安装 Docker Compose"
        exit 1
    fi
    
    log_success "依赖检查通过"
}

check_docker_daemon() {
    if ! docker ps &> /dev/null; then
        log_error "Docker 守护进程未运行，请启动 Docker"
        exit 1
    fi
    
    log_success "Docker 守护进程正在运行"
}

# ============================================================================
# 环境配置
# ============================================================================
setup_compose_env() {
    local docker_dir="$SCRIPT_DIR/docker"
    
    if [ ! -f "$docker_dir/.env" ]; then
        log_error "找不到 docker/.env 配置文件"
        exit 1
    fi
    
    log_info "使用 docker/.env 配置文件"
    
    # 导出环境变量以供 docker-compose 使用
    export COMPOSE_PROFILES="$PROFILES"
    export DOC_ENGINE="$DOC_ENGINE"
    export DEVICE="$DEVICE"
    
    log_info "中间件配置:"
    log_info "  - DOC_ENGINE: $DOC_ENGINE"
    log_info "  - DEVICE: $DEVICE"
    log_info "  - COMPOSE_PROFILES: $PROFILES"
}

# ============================================================================
# 启动服务
# ============================================================================
start_services() {
    local docker_dir="$SCRIPT_DIR/docker"
    local compose_file="$docker_dir/docker-compose-base.yml"
    
    if [ ! -f "$compose_file" ]; then
        log_error "找不到 docker-compose-base.yml"
        exit 1
    fi
    
    echo
    echo "=========================================="
    echo "启动基础中间件服务"
    echo "=========================================="
    echo "Docker Compose 文件: $compose_file"
    echo
    
    cd "$docker_dir"
    
    # 启动容器
    log_info "启动容器..."
    if docker-compose -f docker-compose-base.yml up -d; then
        log_success "容器启动成功"
    else
        log_error "容器启动失败"
        exit 1
    fi
    
    cd "$SCRIPT_DIR"
}

# ============================================================================
# 健康检查
# ============================================================================
wait_for_services() {
    local max_attempts=120
    local attempt=0
    local failed_services=()
    
    echo
    log_info "等待服务就绪（最多等待 2 分钟）..."
    echo
    
    # 定义要检查的服务
    local services_to_check=()
    
    if [[ "$PROFILES" == *"elasticsearch"* ]] || [[ "$DOC_ENGINE" == "elasticsearch" ]]; then
        services_to_check+=("es01")
    fi
    
    if [[ "$PROFILES" == *"opensearch"* ]] || [[ "$DOC_ENGINE" == "opensearch" ]]; then
        services_to_check+=("opensearch01")
    fi
    
    if [[ "$PROFILES" == *"infinity"* ]] || [[ "$DOC_ENGINE" == "infinity" ]]; then
        services_to_check+=("infinity")
    fi
    
    if [[ "$PROFILES" == *"oceanbase"* ]] || [[ "$DOC_ENGINE" == "oceanbase" ]]; then
        services_to_check+=("oceanbase")
    fi
    
    services_to_check+=("mysql" "minio" "redis")
    
    while [ $attempt -lt $max_attempts ]; do
        failed_services=()
        
        for service in "${services_to_check[@]}"; do
            # 检查容器是否存在且运行中
            if ! docker ps --format "table {{.Names}}" | grep -q "docker-${service}-1"; then
                failed_services+=("$service")
            fi
        done
        
        if [ ${#failed_services[@]} -eq 0 ]; then
            log_success "所有服务已就绪！"
            return 0
        fi
        
        attempt=$((attempt + 1))
        if [ $((attempt % 10)) -eq 0 ]; then
            log_info "等待服务就绪... [${attempt}/${max_attempts}] 未就绪: ${failed_services[*]}"
        fi
        
        sleep 1
    done
    
    log_error "服务启动超时，以下服务未就绪: ${failed_services[*]}"
    log_warn "请运行以下命令查看容器状态:"
    log_warn "  docker-compose -f docker/docker-compose-base.yml ps"
    return 1
}

# ============================================================================
# 显示服务信息
# ============================================================================
show_service_info() {
    echo
    echo "=========================================="
    echo "服务启动信息"
    echo "=========================================="
    echo
    
    local docker_dir="$SCRIPT_DIR/docker"
    
    # 读取 .env 文件，展示关键端口
    if [ -f "$docker_dir/.env" ]; then
        log_info "访问地址:"
        
        if [[ "$DOC_ENGINE" == "elasticsearch" ]]; then
            local es_port=$(grep "^ES_PORT=" "$docker_dir/.env" | cut -d'=' -f2)
            log_info "  - Elasticsearch: http://localhost:${es_port:-9200} (用户名: elastic)"
        fi
        
        if [[ "$DOC_ENGINE" == "opensearch" ]]; then
            local os_port=$(grep "^OS_PORT=" "$docker_dir/.env" | cut -d'=' -f2)
            log_info "  - OpenSearch: http://localhost:${os_port:-9201} (用户名: admin)"
        fi
        
        if [[ "$DOC_ENGINE" == "infinity" ]]; then
            local infinity_http_port=$(grep "^INFINITY_HTTP_PORT=" "$docker_dir/.env" | cut -d'=' -f2)
            log_info "  - Infinity HTTP: http://localhost:${infinity_http_port:-23820}"
        fi
        
        local mysql_port=$(grep "^MYSQL_PORT=" "$docker_dir/.env" | cut -d'=' -f2)
        log_info "  - MySQL: localhost:${mysql_port:-3306} (用户名: root)"
        
        local minio_port=$(grep "^MINIO_PORT=" "$docker_dir/.env" | cut -d'=' -f2)
        local minio_console_port=$(grep "^MINIO_CONSOLE_PORT=" "$docker_dir/.env" | cut -d'=' -f2)
        log_info "  - MinIO API: http://localhost:${minio_port:-9000}"
        log_info "  - MinIO Console: http://localhost:${minio_console_port:-9001}"
        
        local redis_port=$(grep "^REDIS_PORT=" "$docker_dir/.env" | cut -d'=' -f2)
        log_info "  - Redis: localhost:${redis_port:-6379}"
    fi
    
    echo
    log_info "查看容器状态:"
    log_info "  docker-compose -f docker/docker-compose-base.yml ps"
    echo
    log_info "查看服务日志:"
    log_info "  docker-compose -f docker/docker-compose-base.yml logs -f [service_name]"
    echo
    log_info "停止所有服务:"
    log_info "  docker-compose -f docker/docker-compose-base.yml down"
    echo
}

# ============================================================================
# 主函数
# ============================================================================
main() {
    echo "=========================================="
    echo "RAGFlow 基础中间件启动脚本"
    echo "=========================================="
    echo
    
    check_dependencies
    check_docker_daemon
    setup_compose_env
    start_services
    
    if wait_for_services; then
        show_service_info
        log_success "全部服务启动完成！"
        return 0
    else
        log_error "部分服务启动失败，请检查日志"
        return 1
    fi
}

# ============================================================================
# 执行
# ============================================================================
main "$@"
