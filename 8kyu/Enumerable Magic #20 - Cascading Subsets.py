def each_cons(lst, n):
    # your solution here
    ans = []
    
    for i in range(len(lst)-n+1):
        ans.append(lst[i:i+n])
    return ans