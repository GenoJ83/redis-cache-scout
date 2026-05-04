from src.cleaner.pruner import plan_evictions
from src.core.models import KeyMeta

def test_eviction_plan():
    keys = [
        KeyMeta("k1", "str", 1000, -1),
        KeyMeta("k2", "str", 500, 10),
        KeyMeta("k3", "str", 2000, -1)
    ]
    evicted, freed = plan_evictions(keys, target_freed_bytes=1500)
    assert "k3" in evicted
    assert freed >= 1500
