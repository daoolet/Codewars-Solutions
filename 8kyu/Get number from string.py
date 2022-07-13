import re

def get_number_from_string(s):
    return int(re.sub('\D', '', s))