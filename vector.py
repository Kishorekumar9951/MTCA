class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,ob):
        return Vector(self.x+ob.x,self.y+ob.y)
    def __sub__(self,other):
        return Vector(self.x-other.x,self.y-other.y)

first=Vector(5,7)
second=Vector(3,8)
result=first+second
print(result.x)
print(result.y)
result=first-second
print(result.x)
print(result.y)
