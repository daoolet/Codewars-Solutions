def unused_digits(*num):
    lst = [1,2,3,4,5,6,7,8,9,0]
    x = []
    ans = []
    for i in num:
        for j in str(i):
            x.append(int(j))

    for i in lst:
        if i not in x:
            ans.append(i)

    sss = ''.join(sorted([str(i) for i in ans]))
    return sss