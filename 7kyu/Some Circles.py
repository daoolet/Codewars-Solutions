import math

def sum_circles(*args):
    s = 0
    for i in args:
        s += math.pi*(i**2)/4
    return f"We have this much circle: {round(s)}"