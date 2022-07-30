def find_it(a):
    for i in set(a):
        if a.count(i)%2!=0:
            return i 