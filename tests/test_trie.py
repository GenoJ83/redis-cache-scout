from src.trie.prefix_trie import PrefixAnalyzer
from src.core.models import KeyMeta

def test_prefix_analysis():
    analyzer = PrefixAnalyzer(delimiter=":")
    analyzer.insert(KeyMeta("user:101:profile", "hash", 500, 3600))
    analyzer.insert(KeyMeta("user:102:profile", "hash", 700, 3600))
    analyzer.insert(KeyMeta("session:xyz", "string", 200, 300))
    top = analyzer.top_prefixes()
    assert len(top) == 2
    assert top[0].prefix == "user" and top[0].total_bytes == 1200
    assert top[1].prefix == "session" and top[1].total_bytes == 200
