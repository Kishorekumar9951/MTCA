def Jasmine(k):
    s={
        0:"sunday",
        1:"monday",
        2:"tuesday",
        3:"wednesday",
        4:"thursday",
        5:"friday",
        6:"saturday",
        }
    return s.get(k,'INVALID')
inp=int(input())
print(Jasmine(inp))
        
