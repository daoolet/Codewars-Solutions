a = 2
b = 2
res = a+b
s = ''
while res > 0:
    if res%2:
        print('1',end='')
    else:
        print('0',end='')
    res = res// 2

print(s)