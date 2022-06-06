def find_nb(m):
    i = 0
    s = 0
    while s < m:
        i += 1
        s += i ** 3
    return i if s == m else -1