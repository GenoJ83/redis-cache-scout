from src.sampling.scanner import scan_chunks
from src.core.models import KeyMeta

def test_scan_chunks():
    keys = [KeyMeta(f"k{i}", "str", 10, 10) for i in range(12)]
    chunks = list(scan_chunks(keys, batch_size=5))
    assert len(chunks) == 3
    assert len(chunks[0]) == 5 and len(chunks[-1]) == 2
