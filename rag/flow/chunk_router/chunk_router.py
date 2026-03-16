#
#  Custom Operator: ChunkRouter
#  NOT a RAGflow official component — custom extension for MedLinkAI Pipeline
#
#  Purpose: Route chunks by classification type to different output keys
#  Auto-discovered by rag/flow/__init__.py via pkgutil.walk_packages
#
import json
import logging
from copy import deepcopy
from collections import defaultdict
from rag.flow.base import ProcessBase, ProcessParamBase


class ChunkRouterParam(ProcessParamBase):
    """ChunkRouter parameters — NOT a RAGflow official component"""
    def __init__(self):
        super().__init__()
        self.classify_field = "classify_result_tks"
        self.type_json_key = "type"
        self.route_map = {}
        self.default_route = "chunks_Default"

    def check(self):
        # Do NOT call super().check() — base class raises NotImplementedError
        # Custom validation for ChunkRouter params
        return True


class ChunkRouter(ProcessBase):
    """
    Routes chunks by classify field value into different output keys.

    NOT a RAGflow official component — custom extension for MedLinkAI project.

    Input (via kwargs from upstream Classify):
        chunks: list[dict] — each chunk has classify_result_tks field

    Output:
        chunks_{Type}: list[dict] — grouped chunks per type
        route_summary: dict — {type: count} stats
        output_format: "chunks"
        name: str — passthrough
    """
    component_name = "ChunkRouter"

    async def _invoke(self, **kwargs):
        chunks = kwargs.get("chunks", [])
        name = kwargs.get("name", "")
        classify_field = self._param.classify_field
        type_json_key = self._param.type_json_key
        route_map = self._param.route_map
        default_route = self._param.default_route

        groups = defaultdict(list)

        for ck in chunks:
            raw = ck.get(classify_field, "")
            try:
                if isinstance(raw, str):
                    classify_data = json.loads(raw)
                elif isinstance(raw, dict):
                    classify_data = raw
                else:
                    classify_data = {}
                doc_type = classify_data.get(type_json_key, "Other")
            except (json.JSONDecodeError, AttributeError, TypeError):
                doc_type = "Other"

            route_key = route_map.get(doc_type, default_route)
            groups[route_key].append(deepcopy(ck))

        route_summary = {}
        for route_key, group_chunks in groups.items():
            self.set_output(route_key, group_chunks)
            route_summary[route_key] = len(group_chunks)

        # Also output all chunks as-is for backward compat
        self.set_output("chunks", chunks)
        self.set_output("output_format", "chunks")
        self.set_output("name", name)
        self.set_output("route_summary", route_summary)

        msg = f"Routed {len(chunks)} chunks into {len(groups)} groups: {route_summary}"
        logging.info(f"[ChunkRouter] {msg}")
        self.callback(1.0, msg)
