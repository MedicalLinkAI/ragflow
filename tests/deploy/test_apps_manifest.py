"""Contract tests for apps.yml manifest completeness."""

import re
from urllib.parse import urlparse

import yaml


REQUIRED_FIELDS = [
    "app_id",
    "compose_service",
    "default_host_ports",
    "health_target",
    "depends_on_app_ids",
    "exposure_class",
    "required_env_groups",
    "secret_inputs",
    "supported_actions",
]


def _load_apps(deploy_dir):
    with open(deploy_dir / "apps.yml") as f:
        return yaml.safe_load(f)["apps"]


def _load_compose_services(deploy_dir):
    with open(deploy_dir / "docker-compose.yml") as f:
        data = yaml.safe_load(f)
    return list(data.get("services", {}).keys())


def _read_script(deploy_dir, name):
    return (deploy_dir / name).read_text()


def _extract_case_branches(script_text):
    """Extract app-id values from bash case statements like:
    ragflow-api|ragflow-web|ragflow-worker)
    or individual branches like:
    ragflow-api)
    """
    branches = set()
    for match in re.finditer(r"([\w-]+(?:\|[\w-]+)*)\)", script_text):
        candidates = match.group(1).split("|")
        for c in candidates:
            if c.startswith("ragflow-"):
                branches.add(c)
    return branches


# --------------------------------------------------------------------------- #
# Tests
# --------------------------------------------------------------------------- #


class TestSchemaCompleteness:
    """Every app entry must have all 9 required fields."""

    def test_all_apps_have_required_fields(self, deploy_dir):
        apps = _load_apps(deploy_dir)
        for app in apps:
            app_id = app.get("app_id", "<unknown>")
            for field in REQUIRED_FIELDS:
                assert field in app, (
                    f"App '{app_id}' missing required field '{field}'"
                )

    def test_exactly_9_required_fields(self):
        assert len(REQUIRED_FIELDS) == 9


class TestComposeServiceAlignment:
    """Every compose_service in apps.yml must exist in docker-compose.yml."""

    def test_services_exist_in_compose(self, deploy_dir):
        apps = _load_apps(deploy_dir)
        compose_services = _load_compose_services(deploy_dir)
        for app in apps:
            svc = app["compose_service"]
            assert svc in compose_services, (
                f"compose_service '{svc}' (app_id={app['app_id']}) "
                f"not found in docker-compose.yml services"
            )


class TestScriptCoverage:
    """build.sh and deploy.sh must handle all app-ids from apps.yml."""

    def test_build_sh_covers_all_app_ids(self, deploy_dir):
        apps = _load_apps(deploy_dir)
        app_ids = {a["app_id"] for a in apps}
        script = _read_script(deploy_dir, "build.sh")
        branches = _extract_case_branches(script)
        missing = app_ids - branches
        assert not missing, f"build.sh missing case branches for: {missing}"

    def test_deploy_sh_covers_all_app_ids(self, deploy_dir):
        apps = _load_apps(deploy_dir)
        app_ids = {a["app_id"] for a in apps}
        script = _read_script(deploy_dir, "deploy.sh")
        branches = _extract_case_branches(script)
        missing = app_ids - branches
        assert not missing, f"deploy.sh missing case branches for: {missing}"


class TestHealthTargetFormat:
    """health_target must be a valid URL or empty string (for workers)."""

    def test_health_targets_valid(self, deploy_dir):
        apps = _load_apps(deploy_dir)
        for app in apps:
            target = app["health_target"]
            if target == "":
                # Empty is valid for workers with no HTTP endpoint
                continue
            # Allow shell variable interpolation in URLs — strip ${...} for parse
            sanitized = re.sub(r"\$\{[^}]+\}", "12345", target)
            parsed = urlparse(sanitized)
            assert parsed.scheme in ("http", "https"), (
                f"App '{app['app_id']}' health_target has invalid scheme: "
                f"'{parsed.scheme}' in '{target}'"
            )
            assert parsed.hostname, (
                f"App '{app['app_id']}' health_target missing hostname: "
                f"'{target}'"
            )

    def test_worker_has_empty_health_target(self, deploy_dir):
        apps = _load_apps(deploy_dir)
        worker = next(a for a in apps if a["app_id"] == "ragflow-worker")
        assert worker["health_target"] == "", (
            "ragflow-worker should have empty health_target (no HTTP endpoint)"
        )
