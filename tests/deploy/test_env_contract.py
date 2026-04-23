def _read_env(path):
    env = {}
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        env[key.strip()] = value.strip()
    return env


class TestTestEnvContract:
    def test_test_env_uses_test_scoped_images_and_callback(self, deploy_dir):
        env = _read_env(deploy_dir / ".env.test")

        assert env["DEPLOY_ENV"] == "test"
        assert env["COMPOSE_PROJECT_NAME"] == "ragflow-test"
        assert env["RAGFLOW_IMAGE"] == "ragflow:test"
        assert env["RAGFLOW_WEB_IMAGE"] == "ragflow-web:test"
        assert env["SYNC_CALLBACK_URL"] == "http://medlinkai-test-callback:8000/api/v1/sync/chunks"

    def test_web_service_uses_env_scoped_image_setting(self, deploy_dir):
        text = (deploy_dir / "docker-compose.yml").read_text()
        assert 'image: ${RAGFLOW_WEB_IMAGE:-ragflow-web:latest}' in text

    def test_build_and_deploy_scripts_reference_env_scoped_web_image(self, deploy_dir):
        build_text = (deploy_dir / "build.sh").read_text()
        deploy_text = (deploy_dir / "deploy.sh").read_text()
        assert "RAGFLOW_WEB_IMAGE" in build_text
        assert "RAGFLOW_WEB_IMAGE" in deploy_text
