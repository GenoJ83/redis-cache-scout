from src.metrics.prom import to_prometheus

def test_prom_export():
    metrics = to_prometheus({"total_keys": 50, "total_bytes": 102400})
    assert "redis_scout_total_keys 50" in metrics
    assert "redis_scout_total_bytes 102400" in metrics
