import math
def find_difference(a, b):
    return math.prod(a)-math.prod(b) if math.prod(b) < math.prod(a) else math.prod(b) - math.prod(a)