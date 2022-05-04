def bingo(array): 
    bingo = [2,9,14,7,15]
    c = 0
    
    for i in bingo:
        if i in array:
            c+=1
    if c == 5:
        return "WIN"
    else:
        return "LOSE"