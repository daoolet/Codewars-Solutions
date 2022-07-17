import re

def disemvowel(s):
    return re.sub('[aeuioAEUIO]', '', s)