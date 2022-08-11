
def duplicate_count(s):

    return sum(1 for i in set(s.lower()) if s.lower().count(i) > 1)
