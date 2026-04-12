from typing import Dict, List, Tuple

class HotKeyTracker:
    def __init__(self):
        self.hits: Dict[str, int] = {}
        
    def record_access(self, key: str) -> None:
        self.hits[key] = self.hits.get(key, 0) + 1
        
    def top_hot_keys(self, limit: int = 10) -> List[Tuple[str, int]]:
        return sorted(self.hits.items(), key=lambda x: x[1], reverse=True)[:limit]
