# redis-cache-scout

Redis keyspace memory profiler, idle key cleaner, prefix tree analyzer, and hot key access tracker without blocking the event loop.

[![CI](https://github.com/GenoJ83/redis-cache-scout/actions/workflows/ci.yml/badge.svg)](https://github.com/GenoJ83/redis-cache-scout/actions)

## Features
- **Namespace Prefix Trie**: Hierarchically clusters memory usage by colon/slash delimiters
- **TTL Expiration Auditor**: Flags dangerous persistent keys and groups cache lifespans
- **BigKey & Stale Key Detector**: Identifies memory hogs and unread idle data
- **Safe Eviction Planner**: Computes optimal keys to prune for target memory budgets

## Quick Start
```python
from src.scout import RedisCacheScout
from src.core.models import KeyMeta

keys = [
    KeyMeta('user:1:profile', 'hash', 1024, 3600),
    KeyMeta('user:2:profile', 'hash', 1024, 3600),
    KeyMeta('session:abc', 'string', 256, 300),
]
scout = RedisCacheScout(keys)
summary = scout.analyze()
print(f"Total memory: {summary['total_bytes']} bytes across {summary['total_keys']} keys")
```
