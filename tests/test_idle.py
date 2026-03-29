from src.idle.finder import find_idle_keys
from src.core.models import KeyMeta

def test_idle_keys():
    k1 = KeyMeta("active", "str", 10, 60, idle_seconds=100)
    k2 = KeyMeta("stale", "str", 10, 60, idle_seconds=1000000)
    stale = find_idle_keys([k1, k2], min_idle_seconds=500000)
    assert len(stale) == 1 and stale[0].key == "stale"
