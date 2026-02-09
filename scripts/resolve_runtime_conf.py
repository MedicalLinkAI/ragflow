#!/usr/bin/env python3
"""Resolve active runtime config for shell scripts.

Outputs shell-safe KEY=VALUE lines so bash scripts can eval them.
"""

import argparse
import shlex
import sys
from pathlib import Path
from urllib.parse import urlparse

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from common.config_utils import read_config_with_meta  # noqa: E402


def split_host_port(value, default_port):
    if value is None:
        return "localhost", str(default_port)

    text = str(value).strip()
    if not text:
        return "localhost", str(default_port)

    if "://" in text:
        parsed = urlparse(text)
        host = parsed.hostname or "localhost"
        port = parsed.port or default_port
        return host, str(port)

    if text.startswith("[") and "]" in text:
        # IPv6 in [::1]:6379 format
        right = text.split("]", 1)
        host = right[0].lstrip("[")
        remainder = right[1]
        if remainder.startswith(":"):
            return host, remainder[1:] or str(default_port)
        return host, str(default_port)

    if ":" in text:
        host, port = text.rsplit(":", 1)
        if port.isdigit():
            return host or "localhost", port

    return text, str(default_port)


def parse_es_host(es_hosts, default_port=1200):
    hosts = str(es_hosts or "").strip()
    if not hosts:
        return "localhost", str(default_port)

    first = hosts.split(",", 1)[0].strip()
    return split_host_port(first, default_port)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--format", choices=["shell"], default="shell")
    args = parser.parse_args()

    config, meta = read_config_with_meta()

    ragflow_conf = config.get("ragflow", {}) or {}
    admin_conf = config.get("admin", {}) or {}
    postgres_conf = config.get("postgres", {}) or {}
    mysql_conf = config.get("mysql", {}) or {}
    redis_conf = config.get("redis", {}) or {}
    minio_conf = config.get("minio", {}) or {}
    es_conf = config.get("es", {}) or {}

    redis_host, redis_port = split_host_port(redis_conf.get("host", "localhost:6379"), 6379)
    minio_host, minio_port = split_host_port(minio_conf.get("host", "localhost:9000"), 9000)
    es_host, es_port = parse_es_host(es_conf.get("hosts", "http://localhost:1200"), 1200)

    env = {
        "ACTIVE_ENV": meta.get("active_env") or "default",
        "ACTIVE_CONF_NAME": meta.get("active_conf_name") or "service_conf.yaml",
        "ACTIVE_CONF_PATH": meta.get("active_conf_path") or "",
        "APPLIED_CONF_PATHS": ",".join(meta.get("applied_conf_paths") or []),
        "LOCAL_CONF_PATHS": ",".join(meta.get("local_conf_paths") or []),
        "RAGFLOW_HOST": str(ragflow_conf.get("host", "0.0.0.0")),
        "RAGFLOW_PORT": str(ragflow_conf.get("http_port", 9380)),
        "ADMIN_HOST": str(admin_conf.get("host", "0.0.0.0")),
        "ADMIN_PORT": str(admin_conf.get("http_port", 9381)),
        "POSTGRES_HOST": str(postgres_conf.get("host", "localhost")),
        "POSTGRES_PORT": str(postgres_conf.get("port", 5432)),
        "MYSQL_HOST": str(mysql_conf.get("host", "localhost")),
        "MYSQL_PORT": str(mysql_conf.get("port", 3306)),
        "REDIS_HOST": redis_host,
        "REDIS_PORT": redis_port,
        "REDIS_DB": str(redis_conf.get("db", 0)),
        "MINIO_HOST": minio_host,
        "MINIO_PORT": minio_port,
        "MINIO_BUCKET": str(minio_conf.get("bucket", "ragflow")),
        "ES_HOST": es_host,
        "ES_PORT": es_port,
    }

    if args.format == "shell":
        for key, value in env.items():
            print(f"{key}={shlex.quote(value)}")


if __name__ == "__main__":
    main()
