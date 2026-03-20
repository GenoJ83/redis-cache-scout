from typing import List, Dict, Any
from src.core.models import KeyMeta

def aggregate_by_type(keys: List[KeyMeta]) -> Dict[str, Dict[str, Any]]:
    agg: Dict[str, Dict[str, Any]] = {}
    for k in keys:
        t = k.type_name.lower()
        if t not in agg:
            agg[t] = {"count": 0, "total_bytes": 0}
        agg[t]["count"] += 1
        agg[t]["total_bytes"] += k.size_bytes
    return agg
