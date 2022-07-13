import re

def is_lock_ness_monster(s):
    return bool(re.search(r'(tree fiddy|three fifty|3\.50)', s))