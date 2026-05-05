from src.bigkeys.detector import find_large_keys
from src.core.models import KeyMeta

def test_large_keys():
    k1 = KeyMeta("normal", "str", 100, 10)
    k2 = KeyMeta("huge", "hash", 2000000, 10)
    big = find_large_keys([k1, k2], threshold_bytes=1000000)
    assert len(big) == 1 and big[0].key == "huge"
