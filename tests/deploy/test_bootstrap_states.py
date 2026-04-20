"""Contract tests for setup.sh bootstrap 4-state machine."""

import re


def _read_setup_sh(deploy_dir):
    return (deploy_dir / "setup.sh").read_text()


# --------------------------------------------------------------------------- #
# Tests
# --------------------------------------------------------------------------- #

BOOTSTRAP_STATES = ["initialized", "skipped-existing", "repair-required", "failed"]


class TestBootstrapStatesPresent:
    """setup.sh must declare all 4 bootstrap states."""

    def test_all_states_present(self, deploy_dir):
        script = _read_setup_sh(deploy_dir)
        for state in BOOTSTRAP_STATES:
            assert state in script, (
                f"Bootstrap state '{state}' not found in setup.sh"
            )


class TestExitCodeContract:
    """Exit codes: initialized/skipped-existing → 0, failed → 1, repair-required → 2."""

    def test_success_states_exit_zero(self, deploy_dir):
        script = _read_setup_sh(deploy_dir)
        # Look for exit_code=0 associated with initialized / skipped-existing
        # The script sets status and exit_code in output_status()
        assert re.search(
            r'status="initialized".*?exit_code=0',
            script,
            re.DOTALL,
        ), "initialized should map to exit_code=0"

        assert re.search(
            r'status="skipped-existing".*?exit_code=0',
            script,
            re.DOTALL,
        ), "skipped-existing should map to exit_code=0"

    def test_failed_exits_one(self, deploy_dir):
        script = _read_setup_sh(deploy_dir)
        assert re.search(
            r'status="failed".*?exit_code=1',
            script,
            re.DOTALL,
        ), "failed should map to exit_code=1"

    def test_repair_required_exits_two(self, deploy_dir):
        script = _read_setup_sh(deploy_dir)
        assert re.search(
            r'status="repair-required".*?exit_code=2',
            script,
            re.DOTALL,
        ), "repair-required should map to exit_code=2"


class TestJsonOutput:
    """setup.sh must output JSON status."""

    def test_json_status_line(self, deploy_dir):
        script = _read_setup_sh(deploy_dir)
        # Script uses escaped quotes: {\"status\":\"...\",\"timestamp\":...}
        assert re.search(
            r'\{.*status.*timestamp.*components.*\}',
            script,
        ), "setup.sh should output a JSON line with status, timestamp, components"


class TestInfraComponentChecks:
    """setup.sh must check all 4 infra components."""

    INFRA_COMPONENTS = ["elasticsearch", "postgres", "redis", "minio"]

    def test_all_infra_components_checked(self, deploy_dir):
        script = _read_setup_sh(deploy_dir)
        for comp in self.INFRA_COMPONENTS:
            assert comp in script, (
                f"Infra component '{comp}' not referenced in setup.sh"
            )

    def test_infra_components_array(self, deploy_dir):
        """The INFRA_COMPONENTS array should list all 4 components."""
        script = _read_setup_sh(deploy_dir)
        match = re.search(r'INFRA_COMPONENTS=\(([^)]+)\)', script)
        assert match, "INFRA_COMPONENTS array not found in setup.sh"
        array_content = match.group(1)
        for comp in self.INFRA_COMPONENTS:
            assert f'"{comp}"' in array_content, (
                f"'{comp}' not in INFRA_COMPONENTS array"
            )
