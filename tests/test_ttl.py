from src.ttl.auditor import TTLAuditor
from src.core.models import KeyMeta

def test_ttl_distribution():
    keys = [
        KeyMeta("k1", "string", 10, -1),
        KeyMeta("k2", "string", 10, 600),
        KeyMeta("k3", "string", 10, 7200),
        KeyMeta("k4", "string", 10, 100000)
    ]
    dist = TTLAuditor.compute_distribution(keys)
    assert dist["persistent_no_ttl"] == 1
    assert dist["under_1_hour"] == 1
    assert dist["1_to_24_hours"] == 1
    assert dist["over_24_hours"] == 1
