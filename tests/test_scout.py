from src.scout import RedisCacheScout
from src.core.models import KeyMeta

def test_scout_analysis():
    keys = [KeyMeta("cache:v1:user", "hash", 2048, 3600)]
    scout = RedisCacheScout(keys)
    rep = scout.analyze()
    assert rep["total_keys"] == 1
    assert rep["total_bytes"] == 2048
    assert len(rep["top_prefixes"]) == 1
