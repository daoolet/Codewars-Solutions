
def find_missing(a):
    d = (a[len(a)-1] - a[0]) // len(a)
    
    return sum(a[0] + d*i for i in range(len(a)+1)) - sum(a)

