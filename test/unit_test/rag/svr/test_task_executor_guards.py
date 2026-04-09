#
#  Copyright 2026 The InfiniFlow Authors. All Rights Reserved.
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
import importlib
import sys
import types
import warnings
from types import SimpleNamespace

import numpy as np
import pytest

warnings.filterwarnings(
    "ignore",
    message="pkg_resources is deprecated as an API.*",
    category=UserWarning,
)
warnings.filterwarnings(
    "ignore",
    message="Tensorflow not installed; ParametricUMAP will be unavailable",
    category=ImportWarning,
)


def _install_xgboost_stub_if_unavailable():
    if "xgboost" in sys.modules:
        return
    try:
        importlib.import_module("xgboost")
        sys.modules["xgboost"] = types.ModuleType("xgboost")
    except Exception:
        sys.modules["xgboost"] = types.ModuleType("xgboost")


_install_xgboost_stub_if_unavailable()

from rag.svr import task_executor


def test_build_raptor_chunk_skips_missing_vector():
    assert task_executor._build_raptor_chunk({"content_with_weight": "demo"}, "q_768_vec", "doc-1") is None


def test_build_raptor_chunk_returns_content_and_vector_array():
    chunk = task_executor._build_raptor_chunk(
        {"content_with_weight": "demo", "q_768_vec": [1.0, 2.0]},
        "q_768_vec",
        "doc-1",
    )

    assert chunk[0] == "demo"
    assert np.array_equal(chunk[1], np.array([1.0, 2.0]))


@pytest.mark.asyncio
async def test_cleanup_canceled_task_doc_uses_index_exist(monkeypatch):
    calls = []
    monkeypatch.setattr(task_executor.search, "index_name", lambda tenant_id: f"idx-{tenant_id}")
    monkeypatch.setattr(
        task_executor.settings,
        "docStoreConn",
        SimpleNamespace(
            index_exist=lambda index_name, kb_id: calls.append(("index_exist", index_name, kb_id)) or True,
            delete=lambda query, index_name, kb_id: calls.append(("delete", query, index_name, kb_id)),
        ),
    )

    await task_executor._cleanup_canceled_task_doc("task-1", "tenant-1", "kb-1", "doc-1")

    assert calls == [
        ("index_exist", "idx-tenant-1", "kb-1"),
        ("delete", {"doc_id": "doc-1"}, "idx-tenant-1", "kb-1"),
    ]
