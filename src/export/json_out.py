import json
from typing import Dict, Any

def export_json(analysis: Dict[str, Any]) -> str:
    cleaned = dict(analysis)
    cleaned["top_prefixes"] = [
        {"prefix": p.prefix, "key_count": p.key_count, "total_bytes": p.total_bytes}
        for p in analysis["top_prefixes"]
    ]
    return json.dumps(cleaned, indent=2)
