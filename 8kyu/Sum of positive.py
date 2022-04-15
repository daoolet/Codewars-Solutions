def positive_sum(arr):
    s = 0
    for i in arr:
        if i > 0:
            s += i
    return s