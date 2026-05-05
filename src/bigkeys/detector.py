from typing import List
from src.core.models import KeyMeta

def find_large_keys(keys: List[KeyMeta], threshold_bytes: int = 1048576) -> List[KeyMeta]:
    return [k for k in keys if k.size_bytes >= threshold_bytes]
