
from functools import reduce

def count_specMult(limit, n):
    primes = [2]

    for i in range(3,101,2):
        k = 0
        q = int(i**0.5)+2

        for j in primes:
            if j > q:
                break
            if i%j == 0:
                k = 1
                break

        if k == 0:
            primes.append(i)

    primes = primes[:limit]

    product = reduce((lambda x, y: x*y), primes)

    return n//product

print(count_specMult(4, 500)) #6