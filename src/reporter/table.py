from typing import Dict, Any

class TerminalReport:
    @staticmethod
    def render(analysis: Dict[str, Any]) -> str:
        lines = [
            f"=== REDIS KEYSPACE AUDIT ===",
            f"Total Keys: {analysis['total_keys']}",
            f"Total Memory: {analysis['total_bytes']} Bytes",
            f"--- TOP PREFIXES ---"
        ]
        for p in analysis["top_prefixes"][:5]:
            lines.append(f"• {p.prefix}: {p.key_count} keys ({p.total_bytes} B)")
        return "\n".join(lines)
