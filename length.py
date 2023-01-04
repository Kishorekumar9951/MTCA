def Jasmine(k):
    lst=k.split()
    return[len(i) for i in lst]
inp=input()
print(*Jasmine(inp))
