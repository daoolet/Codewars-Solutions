def solve(s):
    uc = 0
    lc = 0
    n = 0
    ch = 0
    for i in s:
        if i.isupper():
            uc += 1
        elif i.islower():
            lc += 1
        elif i.isdigit():
            n += 1
        else:
            ch += 1
    return [uc, lc, n, ch]