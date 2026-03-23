from typing import List
from src.core.models import KeyMeta

def find_idle_keys(keys: List[KeyMeta], min_idle_seconds: int = 86400 * 7) -> List[KeyMeta]:
    return [k for k in keys if k.idle_seconds >= min_idle_seconds]
