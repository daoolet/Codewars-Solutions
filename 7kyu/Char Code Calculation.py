def calc(s: str) -> int:

    transduced = ''.join([str(ord(i)) for i in s])
    total1 = transduced
    total2 = transduced.replace('7', '1')

    total1 = sum(int(i) for i in total1)
    if total2 != '':
        total2 = sum(int(i) for i in total2)
    else:
        return 0

    return total1-total2