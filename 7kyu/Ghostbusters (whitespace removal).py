import re

def ghostbusters(building):
    return "You just wanted my autograph didn't you?" if len(building) == len(re.sub('\s', '', building)) else re.sub('\s', '', building) 