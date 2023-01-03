class Number:
    def __init__(self,k):
        self.k=k
    def SumofDigits(self):
        temp=str(self.k)
        t=0
        for i in temp:
            t+=int(i)
        return t
        
inp=int(input())
obj=Number(inp)
print(obj.SumofDigits())
