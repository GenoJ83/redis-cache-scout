class RedisScoutError(Exception):
    """Base exception."""

class ConnectionTimeoutError(RedisScoutError):
    """Raised when Redis probe times out."""

class MemoryThresholdExceededError(RedisScoutError):
    """Raised when keyspace memory exceeds limit."""
