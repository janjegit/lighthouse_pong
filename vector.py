import math

class Vector2D:
    def __init__(self,x=0.0,y=0.0):
        self.x = round(x,5)
        self.y = round(y,5)
    
    def norm(self):
        x = self.x / self.mag()
        y = self.y / self.mag()
        return Vector2D(x,y)

    def mag(self):
        return math.sqrt(pow(self.x,2) + pow(self.y,2))

    def __add__(self,other):
        x = self.x + other.x 
        y = self.y + other.y
        return Vector2D(x,y)

    def __sub__(self,other):
        x = self.x - other.x 
        y = self.y - other.y
        return Vector2D(x,y)

    def __mul__(self,other):
        x = self.x * other.x 
        y = self.y * other.y
        return Vector2D(x,y)

    def __str__(self):
        return str((self.x,self.y))

    def fromTuple(t):
        return Vector2D(t[0],t[1])
