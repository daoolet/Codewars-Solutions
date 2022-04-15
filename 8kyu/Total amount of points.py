def points(games):
    x = 0
    for i in list(games):
        if i[0] > i[-1]:
            x+=3
        elif i[0] < i[-1]:
            x+=0
        else:
            x+=1
    return x