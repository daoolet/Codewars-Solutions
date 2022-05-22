def first_non_consecutive(arr):
    x = None
    for i in range(arr[0],arr[-1]+1):
        if i not in arr:
            x = i +1
            break

    return x