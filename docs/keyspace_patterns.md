# Redis Keyspace Design Best Practices

- Always configure TTL for transient cache keys.
- Use structured colon-separated prefixes: `<service>:<entity>:<id>:<field>`.
- Prevent unbound unbounded collections (sets/hashes) to minimize bigkey spikes.
