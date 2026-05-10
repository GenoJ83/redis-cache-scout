from typing import List, Generator
from src.core.models import KeyMeta

def scan_chunks(keys: List[KeyMeta], batch_size: int = 5) -> Generator[List[KeyMeta], None, None]:
    for i in range(0, len(keys), batch_size):
        yield keys[i:i + batch_size]
