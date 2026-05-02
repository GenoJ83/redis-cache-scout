from typing import List, Tuple
from src.core.models import KeyMeta

def plan_evictions(keys: List[KeyMeta], target_freed_bytes: int) -> Tuple[List[str], int]:
    # Prioritize keys without TTL and largest memory footprint
    candidates = sorted(keys, key=lambda k: (k.ttl_seconds == -1, k.size_bytes), reverse=True)
    to_delete = []
    accum = 0
    for c in candidates:
        to_delete.append(c.key)
        accum += c.size_bytes
        if accum >= target_freed_bytes:
            break
    return to_delete, accum
