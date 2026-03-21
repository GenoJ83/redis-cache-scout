from src.types_agg.types import aggregate_by_type
from src.core.models import KeyMeta

def test_type_agg():
    keys = [
        KeyMeta("k1", "string", 100, 60),
        KeyMeta("k2", "hash", 500, 60),
        KeyMeta("k3", "string", 150, 60)
    ]
    res = aggregate_by_type(keys)
    assert res["string"]["count"] == 2 and res["string"]["total_bytes"] == 250
    assert res["hash"]["count"] == 1 and res["hash"]["total_bytes"] == 500
