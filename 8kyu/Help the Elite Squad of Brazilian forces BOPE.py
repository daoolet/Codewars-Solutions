import math
def mag_number(x):
    
    dct = {
           'PT92': 17, 
           'M4A1': 30, 
           'M16A2': 30, 
           'PSG1': 5
          }


    return math.ceil(x[1]*3/dct[x[0]])