from typing import Dict, Any, List
from src.core.models import KeyMeta, PrefixGroup

class PrefixTrieNode:
    def __init__(self, segment: str = ""):
        self.segment = segment
        self.count = 0
        self.total_bytes = 0
        self.children: Dict[str, "PrefixTrieNode"] = {}

class PrefixAnalyzer:
    def __init__(self, delimiter: str = ":"):
        self.delim = delimiter
        self.root = PrefixTrieNode("root")
        
    def insert(self, key_meta: KeyMeta) -> None:
        parts = key_meta.key.split(self.delim)
        curr = self.root
        for p in parts[:-1]:
            if p not in curr.children:
                curr.children[p] = PrefixTrieNode(p)
            curr = curr.children[p]
            curr.count += 1
            curr.total_bytes += key_meta.size_bytes
            
    def top_prefixes(self) -> List[PrefixGroup]:
        out = []
        for name, node in self.root.children.items():
            out.append(PrefixGroup(prefix=name, key_count=node.count, total_bytes=node.total_bytes, has_persistent_keys=False))
        return sorted(out, key=lambda x: x.total_bytes, reverse=True)
