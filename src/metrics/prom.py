from typing import Dict, Any

def to_prometheus(analysis: Dict[str, Any]) -> str:
    lines = [
        "# HELP redis_scout_total_keys Total keys audited",
        "# TYPE redis_scout_total_keys gauge",
        f"redis_scout_total_keys {analysis['total_keys']}",
        "# HELP redis_scout_total_bytes Total keyspace memory bytes",
        "# TYPE redis_scout_total_bytes gauge",
        f"redis_scout_total_bytes {analysis['total_bytes']}"
    ]
    return "\n".join(lines)
