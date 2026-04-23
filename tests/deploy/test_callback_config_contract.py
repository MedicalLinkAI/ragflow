def _read_file(path):
    return path.read_text()


class TestMedLinkCallbackSeedContract:
    def test_base_sql_uses_env_placeholder_callback_url(self, deploy_dir):
        text = _read_file(deploy_dir / "sql" / "base.sql")
        assert "${SYNC_CALLBACK_URL}" in text
        assert "http://127.0.0.1:18100/api/v1/sync/chunks" not in text
        assert "http://127.0.0.1:8100/api/v1/sync/chunks" not in text

    def test_deploy_script_renders_callback_url_from_env(self, deploy_dir):
        text = _read_file(deploy_dir / "deploy.sh")
        assert "render_base_sql_file" in text
        assert "SYNC_CALLBACK_URL" in text

    def test_deploy_script_has_no_extra_callback_repair_logic(self, deploy_dir):
        text = _read_file(deploy_dir / "deploy.sh")
        assert "repair_medlinkai_sync_chunks_callback_urls" not in text
        assert "MEDLINKAI_SYNC_CHUNKS_URL" not in text
