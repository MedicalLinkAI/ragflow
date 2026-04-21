from pathlib import Path
import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
DEPLOY_DIR = REPO_ROOT / "deploy"


@pytest.fixture
def repo_root():
    return REPO_ROOT


@pytest.fixture
def deploy_dir():
    return DEPLOY_DIR
