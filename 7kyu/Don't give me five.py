def dont_give_me_five(start,end):
    c = 0
    for i in range(start,end+1):
        if i%5 == 0 and (i//5)%2 !=0:
            c+=1
        elif i >= 50 and i < 500:
            if (i//10)%5 == 0 and (i//50)%2 !=0:
                c+=1
                
    return end-start-c+1