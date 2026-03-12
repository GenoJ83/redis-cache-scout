from dataclasses import dataclass
from typing import Optional, Dict, Any

@dataclass
class KeyMeta:
    key: str
    type_name: str
    size_bytes: int
    ttl_seconds: int
    idle_seconds: int = 0
    
@dataclass
class PrefixGroup:
    prefix: str
    key_count: int
    total_bytes: int
    has_persistent_keys: bool
