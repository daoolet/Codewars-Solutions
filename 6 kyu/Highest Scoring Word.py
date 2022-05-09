str = "what time are we climbing up the volcano"
s = 0
summa = []

for word in str.split():
    s = 0
    for i in word:
        s += ord(i)

    summa.append(s)
    print(s, end='**')


print(max(summa))