def count_positives_sum_negatives(arr):
    s=0
    c=0
    if arr != []:
        for i in arr:
            if i <0:
                s+=i
            elif i >0:
                c+=1
        return [c,s]
    else:
        return []