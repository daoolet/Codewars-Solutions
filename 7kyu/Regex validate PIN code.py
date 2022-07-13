import re

def validate_pin(s):
    return bool(re.fullmatch(r'([0-9]{4}|[0-9]{6})', s))