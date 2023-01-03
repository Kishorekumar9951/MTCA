class Number:
    def __init__(self,k):
        self.k=k
    def Even(self):
        if self.k%2==0:
            return "even"
        else:
            return "odd"
inp=int(input())
obj=Number(inp)
print(obj.Even())
