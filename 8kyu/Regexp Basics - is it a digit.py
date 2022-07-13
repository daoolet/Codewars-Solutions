import re

def is_digit(x):
    return True if re.fullmatch(r'^\d$',x) else False