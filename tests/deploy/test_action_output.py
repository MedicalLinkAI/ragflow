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
