from functools import reduce
from math import sqrt

class Vector:

    def __init__(self, coord: list):
        self.coord = coord

    def __str__(self):
        ans = ",".join(map(str, self.coord))
        return f"({ans})"

    def check_len(self, other):
        return len(self.coord) == len(other.coord)
    
    def equals(self, other):
        return self.coord == other.coord
        
    def add(self, other):
        if self.check_len(other):
            ans = [x+y for x, y in zip(self.coord, other.coord)]
            return Vector(ans)
        
    def subtract(self, other):
        if self.check_len(other):
            ans = [x-y for x, y in zip(self.coord, other.coord)]
            return Vector(ans)
        
    def dot(self, other):
        if self.check_len(other):
            ans = [x*y for x, y in zip(self.coord, other.coord)]
            return sum(ans)
    
    def norm(self):
        ans = [i**2 for i in self.coord]
        return sqrt(sum(ans))


a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])

print(a)