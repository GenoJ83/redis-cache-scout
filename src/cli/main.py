import argparse

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="redisscout", description="Redis keyspace memory profiler")
    p.add_argument("--version", action="store_true", help="Print version")
    p.add_argument("--host", default="localhost", help="Redis host")
    p.add_argument("--port", type=int, default=6379, help="Redis port")
    p.add_argument("--delimiter", default=":", help="Key namespace delimiter")
    return p

def main(args=None):
    p = build_parser()
    opts = p.parse_args(args)
    if opts.version:
        print("redisscout v0.1.0")
        return 0
    return 0
