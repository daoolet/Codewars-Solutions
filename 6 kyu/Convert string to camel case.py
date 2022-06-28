import re
def to_camel_case(s: str):
    res = re.split('-|_', s)
    return res[0] + "".join(i.capitalize() for i in res[1:])