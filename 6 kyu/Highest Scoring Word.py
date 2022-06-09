import string

list2  = [i for i in range(1,27)]
list1 = [i for i in string.ascii_lowercase]
dct = dict(zip(list1,list2))

def high(x):
    maxEl = 0

    for index, word in enumerate(x.split()):
        s = 0
        for i in word:
            s += dct[i]
        if s > maxEl:
            maxEl = s
            maxInd = index
            
    return x.split()[maxInd]