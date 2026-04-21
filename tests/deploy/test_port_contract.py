"""Contract tests for port allocation and isolation."""

import re
from collections import Counter

import yaml


def _load_apps(deploy_dir):
    with open(deploy_dir / "apps.yml") as f:
        return yaml.safe_load(f)["apps"]


def _load_env_dev(deploy_dir):
    """Parse .env.dev into a dict of key=value pairs."""
    env = {}
    with open(deploy_dir / ".env.dev") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, _, value = line.partition("=")
                env[key.strip()] = value.strip()
    return env


def _extract_host_ports(env):
    """Return all values whose key ends with _HOST_PORT."""
    return {k: int(v) for k, v in env.items() if k.endswith("_HOST_PORT")}


# --------------------------------------------------------------------------- #
# Tests
# --------------------------------------------------------------------------- #


class TestPortConflicts:
    """No two services may bind the same host port."""

    def test_no_duplicate_ports_in_env_dev(self, deploy_dir):
        env = _load_env_dev(deploy_dir)
        ports = _extract_host_ports(env)
        counts = Counter(ports.values())
        duplicates = {p: n for p, n in counts.items() if n > 1}
        assert not duplicates, f"Port conflicts in .env.dev: {duplicates}"

    def test_no_duplicate_default_ports_in_apps_yml(self, deploy_dir):
        apps = _load_apps(deploy_dir)
        all_ports = []
        for app in apps:
            all_ports.extend(app.get("default_host_ports", []))
        counts = Counter(all_ports)
        duplicates = {p: n for p, n in counts.items() if n > 1}
        assert not duplicates, f"Port conflicts in apps.yml: {duplicates}"


class TestPortIsolation:
    """Dev-env ports must live in the 1xxxx range for isolation."""

    def test_all_dev_ports_in_1xxxx_range(self, deploy_dir):
        env = _load_env_dev(deploy_dir)
        ports = _extract_host_ports(env)
        out_of_range = {
            k: v for k, v in ports.items() if not (10000 <= v <= 19999)
        }
        assert not out_of_range, (
            f"Dev ports outside 1xxxx range: {out_of_range}"
        )


class TestAppsYmlPortsMatchEnvDev:
    """default_host_ports in apps.yml must match .env.dev values."""

    def test_ragflow_api_port(self, deploy_dir):
        apps = _load_apps(deploy_dir)
        env = _load_env_dev(deploy_dir)
        api_app = next(a for a in apps if a["app_id"] == "ragflow-api")
        expected = int(env["RAGFLOW_API_HOST_PORT"])
        assert expected in api_app["default_host_ports"]

    def test_ragflow_web_port(self, deploy_dir):
        apps = _load_apps(deploy_dir)
        env = _load_env_dev(deploy_dir)
        web_app = next(a for a in apps if a["app_id"] == "ragflow-web")
        expected = int(env["RAGFLOW_WEB_HOST_PORT"])
        assert expected in web_app["default_host_ports"]

    def test_ragflow_worker_has_no_ports(self, deploy_dir):
        apps = _load_apps(deploy_dir)
        worker_app = next(a for a in apps if a["app_id"] == "ragflow-worker")
        assert worker_app["default_host_ports"] == [], (
            "ragflow-worker should have no host ports"
        )


class TestCriticalEnvSettings:
    """RAGflow requires DB_TYPE=postgres."""

    def test_db_type_is_postgres(self, deploy_dir):
        env = _load_env_dev(deploy_dir)
        assert env.get("DB_TYPE") == "postgres", (
            f"DB_TYPE must be 'postgres', got '{env.get('DB_TYPE')}'"
        )
