import re
def lowercase_count(s: str):
    return len(re.findall('[a-z]', s))