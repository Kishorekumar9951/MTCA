class Number:
    def __init__(self,k):
        self.k=k
    def Prime(self):
        if self.k<1:
            return 0
        if k==1 or k==2 or k==3:
            return k
        for i in range(2,k):
            if k%i==0:
                return 0
            return k
inp=int(input())
obj=Prime(inp)
print('factorial of',inp,'is',obj.Prime())

