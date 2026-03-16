#
#  Custom Operator: ChunkMerger
#  NOT a RAGflow official component — custom extension for MedLinkAI Pipeline
#
#  Purpose: Merge chunks from multiple upstream Extractors into one output
#  Auto-discovered by rag/flow/__init__.py via pkgutil.walk_packages
#
import logging
from copy import deepcopy
import xxhash
from rag.flow.base import ProcessBase, ProcessParamBase


class ChunkMergerParam(ProcessParamBase):
    """ChunkMerger parameters — NOT a RAGflow official component"""
    def __init__(self):
        super().__init__()
        self.source_components = []   # List of upstream Extract component IDs
        self.chunks_field = "chunks"  # Field name to read from each source

    def check(self):
        # Do NOT call super().check() — base class raises NotImplementedError
        # Custom validation for ChunkMerger params
        return True


class ChunkMerger(ProcessBase):
    """
    Merges chunks from multiple upstream Extractors into a single output.

    NOT a RAGflow official component — custom extension for MedLinkAI project.

    Uses self._canvas.get_variable_value() to pull chunks from each source,
    then cleans self._param.outputs to only keep standard fields
    (prevents Tokenizer's TokenizerFromUpstream extra="forbid" ValidationError).

    Also filters out noise chunks without 'text' field
    (produced by Extractor's else branch when chunks is empty — extractor.py:113).
    """
    component_name = "ChunkMerger"

    async def _invoke(self, **kwargs):
        name = kwargs.get("name", "")

        all_chunks = []
        merge_stats = {}

        for src_id in self._param.source_components:
            try:
                var_expr = f"{src_id}@{self._param.chunks_field}"
                src_chunks = self._canvas.get_variable_value(var_expr)
                if src_chunks and isinstance(src_chunks, list):
                    all_chunks.extend(deepcopy(src_chunks))
                    merge_stats[src_id] = len(src_chunks)
                else:
                    merge_stats[src_id] = 0
            except Exception as e:
                logging.warning(f"[ChunkMerger] Failed to get chunks from {src_id}: {e}")
                merge_stats[src_id] = 0

        # Filter out noise chunks without 'text' field
        # (produced by Extractor else branch when input chunks is empty)
        before_filter = len(all_chunks)
        all_chunks = [ck for ck in all_chunks if ck.get("text")]
        filtered_count = before_filter - len(all_chunks)

        # CRITICAL: Clean self._param.outputs to prevent Tokenizer extra="forbid" error
        # set_output/output operates on self._param.outputs (base.py:453-456)
        # NOT self._outputs (which doesn't exist in the inheritance chain)
        for key in list(self._param.outputs.keys()):
            if key not in ("_created_time", "_elapsed_time"):
                del self._param.outputs[key]

        # Set standard output fields only
        self.set_output("output_format", "chunks")
        self.set_output("chunks", all_chunks)
        self.set_output("name", name)

        # Inject doc_id/kb_id/docnm_kwd/id into each chunk
        # so downstream Invoke:SyncChunks can POST complete data to MedLinkAI.
        # These fields are normally injected by task_executor AFTER Pipeline.run(),
        # but Invoke runs INSIDE Pipeline — so we inject them here.
        doc_id = getattr(self._canvas, '_doc_id', None)
        kb_id = getattr(self._canvas, '_kb_id', None)
        if doc_id:
            for ck in all_chunks:
                ck["doc_id"] = doc_id
                if kb_id:
                    ck["kb_id"] = str(kb_id)
                if name:
                    ck["docnm_kwd"] = name
                if not ck.get("id"):
                    ck["id"] = xxhash.xxh64(
                        (ck["text"] + str(doc_id)).encode("utf-8", "surrogatepass")
                    ).hexdigest()

        msg = (f"Merged {len(all_chunks)} chunks from {len(self._param.source_components)} sources: "
               f"{merge_stats}" + (f" (filtered {filtered_count} noise chunks)" if filtered_count else ""))
        logging.info(f"[ChunkMerger] {msg}")
        self.callback(1.0, msg)
