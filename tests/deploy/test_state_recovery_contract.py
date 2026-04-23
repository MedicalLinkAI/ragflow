import re


def _read_deploy_sh(deploy_dir):
    return (deploy_dir / "deploy.sh").read_text()


class TestStateRecoveryContract:
    def test_missing_state_with_existing_seed_requires_setup_repair(self, deploy_dir):
        script = _read_deploy_sh(deploy_dir)
        assert "base_sql_state_recovery_required" in script
        assert "deploy/setup.sh --env ${ENV}" in script

        match = re.search(
            r'if \[\[ ! -e "\$STATE_FILE" \|\| ! -s "\$STATE_FILE" \]\]; then(.*?)if ! base_sql_pending=',
            script,
            re.DOTALL,
        )
        assert match, "missing-state recovery branch not found in deploy.sh"

        branch = match.group(1)
        assert "update_base_sql_state true false" not in branch
        assert "base_sql_state_recovery_required" in branch
        assert "状态文件缺失或为空" in branch
        assert "不完整的 infra 状态" in branch
        assert '"status":"failed","reason":"base_sql_state_recovery_required"' in branch
        assert "exit 1" in branch
