
def parts_sums(ls):
    summa = sum(ls)
    ans = []
    for i in ls:
        ans.append(summa)
        summa -=i
    return ans + [0]
