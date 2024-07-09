def odd_row(x: int) -> list:
    first = 1
    for i in range(x):
        first += i * 2

    answer = [first]

    for i in range(x):
        first += 2
        answer.append(first)

    return answer[:-1]

print(odd_row(4))

# 1 [1] 1
# 2 [3, 5] 3
# 3 [7, 9, 11] 6
# 4 [13, 15, 17, 19] 10
# 5 [21, 23, 25, 27, 29] 15
# 6 [31, 33, 35, 37, 39, 41] 21

# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# 177553