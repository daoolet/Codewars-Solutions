def c(n, k):
    sum1 = sum2 = 1

    if n-k >= k:
        o = 2
        for i in range(n-k+1,n+1):
            sum1 *= i

            if (sum1 % o ==0 and o<=k):
                sum1= sum1//o
                o+=1
        for i in range(o,k+1):
            sum2 *= i
    else:
        o = 2
        for i in range(k+1,n+1):
            sum1 *= i
            if (sum1 % o == 0 and o<=n-k):
                sum1 = sum1//o
                o += 1
        for i in range(o,n-k+1):
            sum2 *= i

    return sum1//sum2

def use_all_symbols(n, a):
    ans = 0
    for k in range(0, a):
        ans += (-1)**k * c(a,k) * (a-k)**n

    return ans