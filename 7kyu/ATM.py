dol = [500,200,100,50,20,10]
n = 1500
k = 0
for i in dol:
    if n%i:
        k+=1
        n-=n%i

print(k)
                