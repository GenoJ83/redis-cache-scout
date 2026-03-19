from typing import List, Dict
from src.core.models import KeyMeta

class TTLAuditor:
    @staticmethod
    def compute_distribution(keys: List[KeyMeta]) -> Dict[str, int]:
        dist = {
            "persistent_no_ttl": 0,
            "under_1_hour": 0,
            "1_to_24_hours": 0,
            "over_24_hours": 0
        }
        for k in keys:
            if k.ttl_seconds < 0:
                dist["persistent_no_ttl"] += 1
            elif k.ttl_seconds <= 3600:
                dist["under_1_hour"] += 1
            elif k.ttl_seconds <= 86400:
                dist["1_to_24_hours"] += 1
            else:
                dist["over_24_hours"] += 1
        return dist
