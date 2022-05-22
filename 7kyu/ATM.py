def solve(n):
    dol = [500,200,100,50,20,10]
    i = 0
    c = 0
    
    if n%10 == 0:
        while n != 0:
            if n//dol[i] >= 1:
                n -= dol[i]
                c+=1
            else:
                i+=1

        return c
    else:
        return -1