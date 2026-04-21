"""Contract tests for build.sh / deploy.sh action output."""

import re

import yaml


def _read_script(deploy_dir, name):
    return (deploy_dir / name).read_text()


def _load_apps(deploy_dir):
    with open(deploy_dir / "apps.yml") as f:
        return yaml.safe_load(f)["apps"]


# --------------------------------------------------------------------------- #
# Tests
# --------------------------------------------------------------------------- #


class TestBuildShJsonOutput:
    """build.sh must output machine-readable JSON on success."""

    def test_build_json_pattern_present(self, deploy_dir):
        """build.sh should contain JSON output lines with app_id, image, status."""
        script = _read_script(deploy_dir, "build.sh")
        # Scripts use escaped quotes (\") in echo statements
        assert re.search(
            r'\{.*app_id.*image.*status.*\}',
            script,
        ), "build.sh should output JSON with app_id, image, status"

    def test_worker_outputs_skipped(self, deploy_dir):
        """ragflow-worker build should output status 'skipped' (shared image)."""
        script = _read_script(deploy_dir, "build.sh")
        # Scripts use escaped quotes (\") in echo statements
        assert re.search(
            r'ragflow-worker.*status.*skipped',
            script,
        ), "ragflow-worker build should output status='skipped'"

    def test_build_handles_all_app_ids(self, deploy_dir):
        """build.sh case statement must cover all app-ids from apps.yml."""
        apps = _load_apps(deploy_dir)
        app_ids = {a["app_id"] for a in apps}
        script = _read_script(deploy_dir, "build.sh")
        for app_id in app_ids:
            assert app_id in script, (
                f"build.sh does not handle app-id '{app_id}'"
            )

    def test_build_uses_direct_docker_build(self, deploy_dir):
        script = _read_script(deploy_dir, "build.sh")
        assert 'docker build' in script
        assert 'NEED_MIRROR' in script
        assert 'Dockerfile.web' in script


class TestDockerfileRuntimeContract:
    """Runtime image must include sources needed by the worker entrypoint."""

    def test_runtime_image_copies_graphrag_sources(self, deploy_dir):
        dockerfile = (deploy_dir.parent / "Dockerfile").read_text()
        assert 'COPY graphrag graphrag' in dockerfile, (
            'Docker runtime image must copy graphrag sources for task_executor'
        )


class TestDeployShJsonOutput:
    """deploy.sh must output machine-readable JSON."""

    def test_deploy_json_pattern_present(self, deploy_dir):
        """deploy.sh should contain JSON output lines with app_id and status."""
        script = _read_script(deploy_dir, "deploy.sh")
        # Scripts use escaped quotes (\") in echo — match either form
        assert re.search(
            r'\{.*app_id.*status.*\}',
            script,
        ), "deploy.sh should output JSON with app_id, status"

    def test_status_output_has_containers_array(self, deploy_dir):
        """deploy.sh --status should output JSON with a containers array."""
        script = _read_script(deploy_dir, "deploy.sh")
        # Escaped-quote form: {\"containers\":[
        assert re.search(
            r'containers.*\[',
            script,
        ), "deploy.sh --status should output JSON with containers array"

    def test_deploy_runs_base_sql_once(self, deploy_dir):
        script = _read_script(deploy_dir, "deploy.sh")
        assert 'run_base_sql_if_needed' in script
        assert 'base_sql_pending' in script
        assert 'base_sql_applied' in script
        assert 'database_has_base_sql_data' in script
        assert 'base_sql_state_missing' in script
        assert 'deploy/sql/base.sql' in script


class TestScriptSafetyContract:
    """Both scripts must use set -euo pipefail."""

    def test_build_sh_strict_mode(self, deploy_dir):
        script = _read_script(deploy_dir, "build.sh")
        assert "set -euo pipefail" in script, (
            "build.sh must use 'set -euo pipefail'"
        )

    def test_deploy_sh_strict_mode(self, deploy_dir):
        script = _read_script(deploy_dir, "deploy.sh")
        assert "set -euo pipefail" in script, (
            "deploy.sh must use 'set -euo pipefail'"
        )

    def test_setup_sh_strict_mode(self, deploy_dir):
        script = _read_script(deploy_dir, "setup.sh")
        assert "set -euo pipefail" in script, (
            "setup.sh must use 'set -euo pipefail'"
        )


class TestBuildAndDeployShContract:
    """build-and-deploy.sh should orchestrate build + deploy safely."""

    def test_script_exists(self, deploy_dir):
        assert (deploy_dir / "build-and-deploy.sh").exists(), (
            "build-and-deploy.sh should exist in deploy/"
        )

    def test_strict_mode_enabled(self, deploy_dir):
        script = _read_script(deploy_dir, "build-and-deploy.sh")
        assert "set -euo pipefail" in script, (
            "build-and-deploy.sh must use 'set -euo pipefail'"
        )

    def test_references_build_and_deploy_scripts(self, deploy_dir):
        script = _read_script(deploy_dir, "build-and-deploy.sh")
        assert "build.sh" in script
        assert "deploy.sh" in script
        assert 'action":"build-and-deploy"' in script

    def test_supports_wrapper_targets(self, deploy_dir):
        script = _read_script(deploy_dir, "build-and-deploy.sh")
        for app_id in ["ragflow-api", "ragflow-web", "ragflow-worker", "ragflow-all"]:
            assert app_id in script, (
                f"build-and-deploy.sh does not reference '{app_id}'"
            )

    def test_worker_wrapper_rebuilds_shared_api_image(self, deploy_dir):
        script = _read_script(deploy_dir, "build-and-deploy.sh")
        assert 'ragflow-worker)' in script
        assert 'run_build "ragflow-api"' in script
