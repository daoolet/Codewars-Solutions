def digital_root(n):
    if len(str(n)) < 2:
        return sum(int(i) for i in str(n))
    else:
        return digital_root(sum(int(i) for i in str(n)))