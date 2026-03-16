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
import asyncio
import datetime
import inspect
import json
import logging
import random
from timeit import default_timer as timer
from agent.canvas import Graph
from api.db.services.document_service import DocumentService
from api.db.services.task_service import has_canceled, TaskService, CANVAS_DEBUG_DOC_ID
from rag.utils.redis_conn import REDIS_CONN


def _trace_component_output(task_id: str, doc_name: str, component_id: str, cpn_obj):
    """Pipeline 节点级 trace — 日志输出每个节点的关键 outputs。
    
    通用规则（不按节点类型分别处理）：
      规则 1: key 以 _ 开头 → 跳过（内部字段）
      规则 2: value 是 list → 只打 len + chunk 类型分布
      规则 3: value 是 str 且 > 200 字符 → 截断
      规则 4: value 是 dict 且 > 500 字符 → 截断
      规则 5: 其他 → 原样输出
    """
    try:
        outputs = cpn_obj.output()
        if not outputs or not isinstance(outputs, dict):
            return

        summary = {}
        for k, v in outputs.items():
            if k.startswith("_"):
                continue
            if isinstance(v, list):
                # chunks 数组：打数量 + 类型分布
                types = {}
                for ck in v:
                    t = "unknown"
                    cr = ck.get("classify_result_tks") if isinstance(ck, dict) else None
                    if cr:
                        try:
                            t = json.loads(cr).get("type", "unknown")
                        except Exception:
                            pass
                    types[t] = types.get(t, 0) + 1
                summary[k] = f"{len(v)} items, types={types}" if types.get("unknown", 0) < len(v) else f"{len(v)} items"
            elif isinstance(v, str) and len(v) > 200:
                summary[k] = v[:200] + f"...({len(v)} chars)"
            elif isinstance(v, dict):
                ds = json.dumps(v, ensure_ascii=False, default=str)
                summary[k] = ds if len(ds) <= 500 else ds[:500] + f"...({len(ds)} chars)"
            else:
                summary[k] = v

        logging.info(
            f"[Trace] task={task_id[:8] if task_id else 'unknown'} | doc={doc_name} | "
            f"{component_id} | outputs={json.dumps(summary, ensure_ascii=False, default=str)}"
        )
    except Exception as e:
        logging.warning(f"[Trace] Failed to trace {component_id}: {e}")


class Pipeline(Graph):
    def __init__(self, dsl: str|dict, tenant_id=None, doc_id=None, task_id=None, flow_id=None):
        if isinstance(dsl, dict):
            dsl = json.dumps(dsl, ensure_ascii=False)
        super().__init__(dsl, tenant_id, task_id)
        if doc_id == CANVAS_DEBUG_DOC_ID:
            doc_id = None
        self._doc_id = doc_id
        self._flow_id = flow_id
        self._kb_id = None
        self._doc_name = "unknown"
        if self._doc_id:
            self._kb_id = DocumentService.get_knowledgebase_id(doc_id)
            if not self._kb_id:
                self._doc_id = None
            else:
                try:
                    e, doc = DocumentService.get_by_id(doc_id)
                    self._doc_name = doc.name if e else self._doc_id[:8]
                except Exception:
                    self._doc_name = self._doc_id[:8]

    def callback(self, component_name: str, progress: float | int | None = None, message: str = "") -> None:
        from common.exceptions import TaskCanceledException
        log_key = f"{self._flow_id}-{self.task_id}-logs"
        timestamp = timer()
        if has_canceled(self.task_id):
            progress = -1
            message += "[CANCEL]"
        try:
            bin = REDIS_CONN.get(log_key)
            obj = json.loads(bin.encode("utf-8"))
            if obj:
                if obj[-1]["component_id"] == component_name:
                    obj[-1]["trace"].append(
                        {
                            "progress": progress,
                            "message": message,
                            "datetime": datetime.datetime.now().strftime("%H:%M:%S"),
                            "timestamp": timestamp,
                            "elapsed_time": timestamp - obj[-1]["trace"][-1]["timestamp"],
                        }
                    )
                else:
                    obj.append(
                        {
                            "component_id": component_name,
                            "trace": [{"progress": progress, "message": message, "datetime": datetime.datetime.now().strftime("%H:%M:%S"), "timestamp": timestamp, "elapsed_time": 0}],
                        }
                    )
            else:
                obj = [
                    {
                        "component_id": component_name,
                        "trace": [{"progress": progress, "message": message, "datetime": datetime.datetime.now().strftime("%H:%M:%S"), "timestamp": timestamp, "elapsed_time": 0}],
                    }
                ]
            if component_name != "END" and self._doc_id and self.task_id:
                percentage = 1.0 / len(self.components.items())
                finished = 0.0
                for o in obj:
                    for t in o["trace"]:
                        if t["progress"] < 0:
                            finished = -1
                            break
                    if finished < 0:
                        break
                    finished += o["trace"][-1]["progress"] * percentage

                msg = ""
                if len(obj[-1]["trace"]) == 1:
                    msg += f"\n-------------------------------------\n[{self.get_component_name(o['component_id'])}]:\n"
                t = obj[-1]["trace"][-1]
                msg += "%s: %s\n" % (t["datetime"], t["message"])
                TaskService.update_progress(self.task_id, {"progress": finished, "progress_msg": msg})
            elif component_name == "END" and not self._doc_id:
                obj[-1]["trace"][-1]["dsl"] = json.loads(str(self))
            REDIS_CONN.set_obj(log_key, obj, 60 * 30)

        except Exception as e:
            logging.exception(e)

        if has_canceled(self.task_id):
            raise TaskCanceledException(message)

    def fetch_logs(self):
        log_key = f"{self._flow_id}-{self.task_id}-logs"
        try:
            bin = REDIS_CONN.get(log_key)
            if bin:
                return json.loads(bin.encode("utf-8"))
        except Exception as e:
            logging.exception(e)
        return []


    async def run(self, **kwargs):
        log_key = f"{self._flow_id}-{self.task_id}-logs"
        try:
            REDIS_CONN.set_obj(log_key, [], 60 * 10)
        except Exception as e:
            logging.exception(e)
        self.error = ""
        if not self.path:
            self.path.append("File")
            cpn_obj = self.get_component_obj(self.path[0])
            await cpn_obj.invoke(**kwargs)
            if cpn_obj.error():
                self.error = "[ERROR]" + cpn_obj.error()
                self.callback(cpn_obj.component_name, -1, self.error)

        if self._doc_id:
            TaskService.update_progress(self.task_id, {
                "progress": random.randint(0, 5) / 100.0,
                "progress_msg": "Start the pipeline...",
                "begin_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})

        idx = len(self.path) - 1
        cpn_obj = self.get_component_obj(self.path[idx])
        idx += 1
        self.path.extend(cpn_obj.get_downstream())

        while idx < len(self.path) and not self.error:
            last_cpn = self.get_component_obj(self.path[idx - 1])
            cpn_obj = self.get_component_obj(self.path[idx])
            logging.info(f"[Pipeline] Executing component [{idx}]: {self.path[idx]} (type={cpn_obj.component_name})")

            async def invoke():
                nonlocal last_cpn, cpn_obj
                if inspect.iscoroutinefunction(cpn_obj.invoke):
                    await cpn_obj.invoke(**last_cpn.output())
                else:
                    await cpn_obj.invoke_async(**last_cpn.output())

            tasks = []
            tasks.append(asyncio.create_task(invoke()))
            await asyncio.gather(*tasks)
            logging.info(f"[Pipeline] Component [{idx}]: {self.path[idx]} finished. error={cpn_obj.error()}")
            _trace_component_output(self.task_id, self._doc_name, self.path[idx], cpn_obj)

            if cpn_obj.error():
                self.error = "[ERROR]" + cpn_obj.error()
                self.callback(cpn_obj._id, -1, self.error)
                break
            idx += 1
            self.path.extend(cpn_obj.get_downstream())

        self.callback("END", 1 if not self.error else -1, json.dumps(self.get_component_obj(self.path[-1]).output(), ensure_ascii=False))

        if not self.error:
            # Return the last component's output that contains chunks data.
            # Side-effect components (e.g. Invoke) don't produce chunks,
            # so we walk backwards to find the actual data-producing component.
            for i in range(len(self.path) - 1, -1, -1):
                out = self.get_component_obj(self.path[i]).output()
                if out and (out.get("chunks") or out.get("json") or out.get("markdown") or out.get("text") or out.get("html")):
                    return out
            return self.get_component_obj(self.path[-1]).output()

        TaskService.update_progress(self.task_id, {
            "progress": -1,
            "progress_msg": f"[ERROR]: {self.error}"})

        return {}
