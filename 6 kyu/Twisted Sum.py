def compute_sum(n):
    s = 0
    for i in range(1, n+1):
        s += i

        if i > 9:
            for j in str(i):
                s += int(j)
            s -= i

    return s