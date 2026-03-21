from typing import List, Dict, Any
from src.core.models import KeyMeta
from src.trie.prefix_trie import PrefixAnalyzer
from src.ttl.auditor import TTLAuditor
from src.types_agg.types import aggregate_by_type

class RedisCacheScout:
    def __init__(self, sample_keys: List[KeyMeta] = None, delimiter: str = ":"):
        self.keys = sample_keys or []
        self.delimiter = delimiter
        
    def analyze(self) -> Dict[str, Any]:
        analyzer = PrefixAnalyzer(delimiter=self.delimiter)
        for k in self.keys:
            analyzer.insert(k)
        top_prefixes = analyzer.top_prefixes()
        ttl_dist = TTLAuditor.compute_distribution(self.keys)
        type_dist = aggregate_by_type(self.keys)
        total_bytes = sum(k.size_bytes for k in self.keys)
        return {
            "total_keys": len(self.keys),
            "total_bytes": total_bytes,
            "top_prefixes": top_prefixes,
            "ttl_distribution": ttl_dist,
            "type_distribution": type_dist
        }
