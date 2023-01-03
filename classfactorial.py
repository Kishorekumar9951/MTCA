class Number:
    def __init__(self,k):
        self.k=k
    def Fact(self):
        if self.k==0:
            return 1
        res=1
        for i in range(1,self.k +1):
            res*=i
        return res
inp=int(input())
obj=Number(inp)
print('factorial of',inp,'is',obj.Fact())
