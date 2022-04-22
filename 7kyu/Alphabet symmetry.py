def solve(arr):
    ans = []
    alph = 'abcdefghijklmnopqrstuvwxyz'
    for slice in arr:
        count = 0
        for i,j in enumerate(slice):
            if i == alph.index(j.lower()):
                count += 1
        ans.append(count)
        
    return ans