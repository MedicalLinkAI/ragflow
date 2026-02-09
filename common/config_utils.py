#
#  Copyright 2025 The InfiniFlow Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

import os
import copy
import logging
import importlib
from filelock import FileLock

from common.file_utils import get_project_base_directory
from common.constants import SERVICE_CONF
from ruamel.yaml import YAML


ENV_NAME_VAR = "RAGFLOW_ENV"
CONF_NAME_VAR = "RAGFLOW_CONF"


def _normalize_env_name(env_name):
    if not env_name:
        return ""
    normalized = env_name.strip().lower()
    aliases = {
        "development": "dev",
        "testing": "test",
        "production": "prod",
    }
    return aliases.get(normalized, normalized)


def _append_unique(items, value):
    if value and value not in items:
        items.append(value)


def _build_env_conf_name(conf_name, env_name):
    root, ext = os.path.splitext(conf_name)
    if not ext:
        ext = ".yaml"
    return f"{root}.{env_name}{ext}"


def load_yaml_conf(conf_path):
    if not os.path.isabs(conf_path):
        conf_path = os.path.join(get_project_base_directory(), conf_path)
    try:
        with open(conf_path) as f:
            yaml = YAML(typ="safe", pure=True)
            return yaml.load(f)
    except Exception as e:
        raise EnvironmentError("loading yaml file config from {} failed:".format(conf_path), e)


def rewrite_yaml_conf(conf_path, config):
    if not os.path.isabs(conf_path):
        conf_path = os.path.join(get_project_base_directory(), conf_path)
    try:
        with open(conf_path, "w") as f:
            yaml = YAML(typ="safe")
            yaml.dump(config, f)
    except Exception as e:
        raise EnvironmentError("rewrite yaml file config {} failed:".format(conf_path), e)


def conf_realpath(conf_name):
    if os.path.isabs(conf_name):
        return conf_name

    project_dir = get_project_base_directory()
    if os.sep in conf_name:
        return os.path.join(project_dir, conf_name)

    return os.path.join(project_dir, "conf", conf_name)


def _load_config_file(conf_path):
    loaded = load_yaml_conf(conf_path)
    if not isinstance(loaded, dict):
        raise ValueError(f'Invalid config file: "{conf_path}".')
    return loaded


def _read_legacy_config(conf_name=SERVICE_CONF):
    """Legacy behavior: load service_conf + local.service_conf only."""
    local_config = {}
    local_path = conf_realpath(f'local.{conf_name}')

    if os.path.exists(local_path):
        local_config = load_yaml_conf(local_path)
        if not isinstance(local_config, dict):
            raise ValueError(f'Invalid config file: "{local_path}".')

    global_config_path = conf_realpath(conf_name)
    global_config = load_yaml_conf(global_config_path)
    if not isinstance(global_config, dict):
        raise ValueError(f'Invalid config file: "{global_config_path}".')

    global_config.update(local_config)
    meta = {
        "active_env": "",
        "active_conf_name": conf_name,
        "active_conf_path": global_config_path,
        "applied_conf_paths": [global_config_path],
        "local_conf_paths": [local_path] if os.path.exists(local_path) else [],
    }
    return global_config, meta


def read_config_with_meta(conf_name=SERVICE_CONF):
    base_conf_path = conf_realpath(conf_name)
    config = _load_config_file(base_conf_path)

    env_name = _normalize_env_name(os.environ.get(ENV_NAME_VAR, ""))
    explicit_conf = (os.environ.get(CONF_NAME_VAR, "") or "").strip()

    applied_conf_paths = [base_conf_path]
    local_conf_paths = []
    active_conf_name = conf_name
    active_conf_path = base_conf_path

    local_candidates = []

    if explicit_conf:
        explicit_conf_path = conf_realpath(explicit_conf)
        explicit_name = os.path.basename(explicit_conf)
        if os.path.exists(explicit_conf_path):
            config.update(_load_config_file(explicit_conf_path))
            _append_unique(applied_conf_paths, explicit_conf_path)
            active_conf_name = explicit_name
            active_conf_path = explicit_conf_path
        else:
            raise FileNotFoundError(f'RAGFLOW_CONF does not exist: "{explicit_conf_path}"')

        _append_unique(local_candidates, f"local.{explicit_name}")
        _append_unique(local_candidates, f"local.{conf_name}")
    else:
        if env_name:
            env_conf_name = _build_env_conf_name(conf_name, env_name)
            env_conf_path = conf_realpath(env_conf_name)
            if os.path.exists(env_conf_path):
                config.update(_load_config_file(env_conf_path))
                _append_unique(applied_conf_paths, env_conf_path)
                active_conf_name = env_conf_name
                active_conf_path = env_conf_path
            else:
                raise FileNotFoundError(f'Env config not found for RAGFLOW_ENV={env_name}: "{env_conf_path}"')

            _append_unique(local_candidates, f"local.{env_conf_name}")

        _append_unique(local_candidates, f"local.{conf_name}")

    for local_name in local_candidates:
        local_path = conf_realpath(local_name)
        if not os.path.exists(local_path):
            continue

        try:
            config.update(_load_config_file(local_path))
            _append_unique(local_conf_paths, local_path)
        except Exception as ex:
            logging.warning("Skip invalid local override %s: %s", local_path, ex)

    meta = {
        "active_env": env_name,
        "active_conf_name": active_conf_name,
        "active_conf_path": active_conf_path,
        "applied_conf_paths": applied_conf_paths,
        "local_conf_paths": local_conf_paths,
    }
    logging.info(
        "Config resolved: env=%s active=%s applied=%s locals=%s",
        meta["active_env"] or "default",
        meta["active_conf_path"],
        meta["applied_conf_paths"],
        meta["local_conf_paths"],
    )
    return config, meta


def read_config(conf_name=SERVICE_CONF):
    strict_selector = bool((os.environ.get(ENV_NAME_VAR) or "").strip() or (os.environ.get(CONF_NAME_VAR) or "").strip())
    try:
        config, _ = read_config_with_meta(conf_name=conf_name)
    except Exception as ex:
        if strict_selector:
            raise
        logging.warning("read_config_with_meta failed, fallback to legacy read_config: %s", ex)
        config, _ = _read_legacy_config(conf_name=conf_name)
    return config


_strict_selector = bool((os.environ.get(ENV_NAME_VAR) or "").strip() or (os.environ.get(CONF_NAME_VAR) or "").strip())
try:
    CONFIGS, CONFIG_META = read_config_with_meta()
except Exception as ex:
    if _strict_selector:
        raise
    logging.warning("Config bootstrap fallback to legacy due to error: %s", ex)
    CONFIGS, CONFIG_META = _read_legacy_config()
ACTIVE_ENV = CONFIG_META["active_env"]
ACTIVE_CONF_NAME = CONFIG_META["active_conf_name"]
ACTIVE_CONF_PATH = CONFIG_META["active_conf_path"]
APPLIED_CONF_PATHS = CONFIG_META["applied_conf_paths"]
LOCAL_CONF_PATHS = CONFIG_META["local_conf_paths"]


def show_configs():
    msg = (
        f"Current configs, env={ACTIVE_ENV or 'default'}, "
        f"active_conf={ACTIVE_CONF_PATH}:"
    )
    if LOCAL_CONF_PATHS:
        msg += f"\n\tlocal_overrides: {LOCAL_CONF_PATHS}"
    for k, v in CONFIGS.items():
        if isinstance(v, dict):
            if "password" in v:
                v = copy.deepcopy(v)
                v["password"] = "*" * 8
            if "access_key" in v:
                v = copy.deepcopy(v)
                v["access_key"] = "*" * 8
            if "secret_key" in v:
                v = copy.deepcopy(v)
                v["secret_key"] = "*" * 8
            if "secret" in v:
                v = copy.deepcopy(v)
                v["secret"] = "*" * 8
            if "sas_token" in v:
                v = copy.deepcopy(v)
                v["sas_token"] = "*" * 8
            if "oauth" in k:
                v = copy.deepcopy(v)
                for key, val in v.items():
                    if "client_secret" in val:
                        val["client_secret"] = "*" * 8
            if "authentication" in k:
                v = copy.deepcopy(v)
                for key, val in v.items():
                    if "http_secret_key" in val:
                        val["http_secret_key"] = "*" * 8
        msg += f"\n\t{k}: {v}"
    logging.info(msg)


def get_base_config(key, default=None):
    if key is None:
        return None
    if default is None:
        default = os.environ.get(key.upper())
    return CONFIGS.get(key, default)


def decrypt_database_password(password):
    encrypt_password = get_base_config("encrypt_password", False)
    encrypt_module = get_base_config("encrypt_module", False)
    private_key = get_base_config("private_key", None)

    if not password or not encrypt_password:
        return password

    if not private_key:
        raise ValueError("No private key")

    module_fun = encrypt_module.split("#")
    pwdecrypt_fun = getattr(
        importlib.import_module(
            module_fun[0]),
        module_fun[1])

    return pwdecrypt_fun(private_key, password)


def decrypt_database_config(database=None, passwd_key="password", name="database"):
    if not database:
        database = get_base_config(name, {})

    database[passwd_key] = decrypt_database_password(database[passwd_key])
    return database


def update_config(key, value, conf_name=SERVICE_CONF):
    conf_path = conf_realpath(conf_name=conf_name)
    if not os.path.isabs(conf_path):
        conf_path = os.path.join(get_project_base_directory(), conf_path)

    with FileLock(os.path.join(os.path.dirname(conf_path), ".lock")):
        config = load_yaml_conf(conf_path=conf_path) or {}
        config[key] = value
        rewrite_yaml_conf(conf_path=conf_path, config=config)
