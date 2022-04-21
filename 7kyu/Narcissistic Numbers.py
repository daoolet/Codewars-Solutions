
""" n = 153 ---> random number
x = [int(a) for a in str(n)] --> seperating digits of number
s = sum(i**len(str(n)) for i in x) --> powering and finding the sum
print(s) """

def is_narcissistic(n):
    return n == sum(i**len(str(n)) for i in [int(a) for a in str(n)])