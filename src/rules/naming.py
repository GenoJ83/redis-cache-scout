import re

VALID_KEY_REGEX = re.compile(r"^[a-zA-Z0-9_:-]+$")

def check_naming_convention(key: str) -> bool:
    return bool(VALID_KEY_REGEX.match(key))
