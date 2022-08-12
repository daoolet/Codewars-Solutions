def foo(x):
    c = 0
    while x >= 5:
        x //= 5
        c += x

    return c
