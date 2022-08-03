

def find_outlier(x):

    rem = 1 if x[0]%2 + x[1]%2 + x[2]%2 < 2 else 0
    
    for i in x: 
        if i%2==rem: 
            return i

print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))