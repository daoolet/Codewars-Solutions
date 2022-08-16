from math import comb

def est_subsets(a: list) -> int:
    c = 0
    ans = []
    
    for i in a:
        for j in a:
            print(i,j)
            c += 1

    return c

print(est_subsets([1, 2, 3, 4]))