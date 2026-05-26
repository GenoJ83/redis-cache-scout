from src.scout import RedisCacheScout
from src.generator.synth import generate_synthetic_keys
from src.reporter.table import TerminalReport
from src.export.json_out import export_json

def test_full_redis_scout_workflow():
    keys = generate_synthetic_keys(30)
    scout = RedisCacheScout(keys)
    audit = scout.analyze()
    assert audit["total_keys"] == 30
    table = TerminalReport.render(audit)
    assert "REDIS KEYSPACE AUDIT" in table
    json_data = export_json(audit)
    assert "total_keys" in json_data
