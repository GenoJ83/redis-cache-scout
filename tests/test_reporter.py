from src.reporter.table import TerminalReport
from src.scout import RedisCacheScout
from src.core.models import KeyMeta

def test_reporter():
    keys = [KeyMeta("session:1", "str", 50, 60)]
    scout = RedisCacheScout(keys)
    rep = scout.analyze()
    txt = TerminalReport.render(rep)
    assert "REDIS KEYSPACE AUDIT" in txt
    assert "Total Keys: 1" in txt
