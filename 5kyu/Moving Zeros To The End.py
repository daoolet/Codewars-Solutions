def move_zeros(a: list):
    for i in a:
        if i == 0:
            a.remove(i)
            a.append(0)
        
    return a