import json
from src.export.json_out import export_json
from src.scout import RedisCacheScout
from src.core.models import KeyMeta

def test_json_export():
    scout = RedisCacheScout([KeyMeta("test:k", "str", 100, 10)])
    data = json.loads(export_json(scout.analyze()))
    assert data["total_keys"] == 1
    assert data["top_prefixes"][0]["prefix"] == "test"
