import random
from typing import List
from src.core.models import KeyMeta

def generate_synthetic_keys(count: int = 20, seed: int = 42) -> List[KeyMeta]:
    rng = random.Random(seed)
    types = ["string", "hash", "list", "set", "zset"]
    prefixes = ["user", "session", "order", "cache"]
    keys = []
    for i in range(count):
        p = rng.choice(prefixes)
        k_type = rng.choice(types)
        sz = rng.randint(50, 5000)
        ttl = rng.choice([-1, 300, 3600, 86400])
        keys.append(KeyMeta(f"{p}:{i}:data", k_type, sz, ttl))
    return keys
