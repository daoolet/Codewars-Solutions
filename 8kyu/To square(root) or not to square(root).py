import math
def square_or_square_root(arr):
    
    ans = []
    
    for i in arr:
        if math.sqrt(i).is_integer():
            ans.append(math.sqrt(i))
        else:
            ans.append(i**2)
    
    return ans