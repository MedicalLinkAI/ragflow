import yaml


def _compose(deploy_dir):
    return yaml.safe_load((deploy_dir / "docker-compose.yml").read_text())


class TestStatefulVolumeContract:
    def test_stateful_services_use_named_volumes(self, deploy_dir):
        compose = _compose(deploy_dir)
        services = compose["services"]

        assert services["ragflow-elasticsearch"]["volumes"] == ["ragflow_esdata:/usr/share/elasticsearch/data"]
        assert services["ragflow-postgres"]["volumes"] == ["ragflow_pgdata:/var/lib/postgresql/data"]
        assert services["ragflow-redis"]["volumes"] == ["ragflow_redisdata:/data"]
        assert services["ragflow-minio"]["volumes"] == ["ragflow_miniodata:/data"]

    def test_compose_defines_named_volumes(self, deploy_dir):
        compose = _compose(deploy_dir)
        volumes = compose["volumes"]
        assert set(volumes) >= {"ragflow_esdata", "ragflow_pgdata", "ragflow_redisdata", "ragflow_miniodata"}

    def test_compose_no_longer_uses_data_root_bind_mounts(self, deploy_dir):
        text = (deploy_dir / "docker-compose.yml").read_text()
        assert "${DATA_ROOT:-./data}/esdata" not in text
        assert "${DATA_ROOT:-./data}/pgdata" not in text
        assert "${DATA_ROOT:-./data}/redisdata" not in text
        assert "${DATA_ROOT:-./data}/miniodata" not in text
