class Rectangle():
    def __init__(self,length,width):
        assert(length>=0 and width>=0),'Invalid'
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length+self.width)
r=int(input())
k=int(input())
try:
    
    s=Rectangle(r,k)
    print(s.area())
    print(s.perimeter())
except AssertionError as obj:
    print(obj)
