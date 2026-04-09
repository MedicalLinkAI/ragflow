import importlib.util
import json
import sys
from pathlib import Path
from types import ModuleType
from unittest.mock import MagicMock


def _load_invoke_module(monkeypatch):
    repo_root = Path(__file__).resolve().parents[4]

    quart = ModuleType("quart")
    quart.make_response = lambda *a, **kw: None
    quart.jsonify = lambda *a, **kw: None
    monkeypatch.setitem(sys.modules, "quart", quart)

    pandas_mod = ModuleType("pandas")
    pandas_mod.DataFrame = type("DataFrame", (), {})
    monkeypatch.setitem(sys.modules, "pandas", pandas_mod)

    deepdoc = ModuleType("deepdoc")
    deepdoc.__path__ = []
    monkeypatch.setitem(sys.modules, "deepdoc", deepdoc)
    deepdoc_parser = ModuleType("deepdoc.parser")
    deepdoc_parser.HtmlParser = MagicMock
    monkeypatch.setitem(sys.modules, "deepdoc.parser", deepdoc_parser)
    monkeypatch.setitem(sys.modules, "xgboost", ModuleType("xgboost"))

    common_pkg = ModuleType("common")
    common_pkg.__path__ = [str(repo_root / "common")]
    monkeypatch.setitem(sys.modules, "common", common_pkg)

    constants_mod = ModuleType("common.constants")

    class _RetCode:
        SUCCESS = 0
        EXCEPTION_ERROR = 100

    constants_mod.RetCode = _RetCode
    monkeypatch.setitem(sys.modules, "common.constants", constants_mod)

    conn_spec = importlib.util.spec_from_file_location("common.connection_utils", repo_root / "common" / "connection_utils.py")
    conn_mod = importlib.util.module_from_spec(conn_spec)
    monkeypatch.setitem(sys.modules, "common.connection_utils", conn_mod)
    conn_spec.loader.exec_module(conn_mod)

    agent_pkg = ModuleType("agent")
    agent_pkg.__path__ = [str(repo_root / "agent")]
    monkeypatch.setitem(sys.modules, "agent", agent_pkg)

    agent_settings = ModuleType("agent.settings")
    agent_settings.FLOAT_ZERO = 1e-8
    agent_settings.PARAM_MAXDEPTH = 5
    monkeypatch.setitem(sys.modules, "agent.settings", agent_settings)

    component_pkg = ModuleType("agent.component")
    component_pkg.__path__ = [str(repo_root / "agent" / "component")]
    monkeypatch.setitem(sys.modules, "agent.component", component_pkg)

    base_spec = importlib.util.spec_from_file_location("agent.component.base", repo_root / "agent" / "component" / "base.py")
    base_mod = importlib.util.module_from_spec(base_spec)
    monkeypatch.setitem(sys.modules, "agent.component.base", base_mod)
    base_spec.loader.exec_module(base_mod)

    invoke_spec = importlib.util.spec_from_file_location("agent.component.invoke", repo_root / "agent" / "component" / "invoke.py")
    invoke_mod = importlib.util.module_from_spec(invoke_spec)
    monkeypatch.setitem(sys.modules, "agent.component.invoke", invoke_mod)
    invoke_spec.loader.exec_module(invoke_mod)

    return invoke_mod


def _make_invoke(module, *, headers, custom_header):
    canvas = MagicMock()
    canvas.get_variable_value = MagicMock(return_value="")
    canvas.is_canceled = MagicMock(return_value=False)

    param = module.InvokeParam.__new__(module.InvokeParam)
    param.url = "http://example.com"
    param.method = "get"
    param.headers = headers
    param.variables = []
    param.proxy = ""
    param.timeout = 60
    param.clean_html = False
    param.datatype = "json"
    param.max_retries = 0
    param.delay_after_error = 0
    param.outputs = {}
    param.inputs = {}
    param.custom_header = custom_header

    inst = module.Invoke.__new__(module.Invoke)
    inst._canvas = canvas
    inst._param = param
    inst._id = "invoke_test"
    return inst


def test_custom_headers_override_static_trace_headers(monkeypatch):
    module = _load_invoke_module(monkeypatch)
    invoke = _make_invoke(
        module,
        headers=json.dumps(
            {
                "traceparent": "00-11111111111111111111111111111111-2222222222222222-01",
                "X-Trace-Id": "1" * 32,
                "X-Static": "static",
            }
        ),
        custom_header={
            "traceparent": "00-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa-bbbbbbbbbbbbbbbb-01",
            "X-Trace-Id": "a" * 32,
        },
    )
    mock_get = MagicMock()
    monkeypatch.setattr(module.requests, "get", mock_get)

    invoke._invoke()

    headers = mock_get.call_args[1]["headers"]
    assert headers["traceparent"] == "00-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa-bbbbbbbbbbbbbbbb-01"
    assert headers["X-Trace-Id"] == "a" * 32
    assert headers["X-Static"] == "static"
