def make_readable(n: int):
    h = m = s = 0
    for i in range(1,n+1):
        s += 1
        if s > 59:
            m += 1
            s = 0
            if m > 59:
                h += 1
                m = 0
    return f"{str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}"