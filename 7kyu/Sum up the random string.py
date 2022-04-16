def sum_from_string(strng):
    for i in strng:
        if not i.isdigit():
            strng=strng.replace(i, ' ')
    
    return sum(int(i) for i in strng.split())