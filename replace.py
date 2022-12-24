'''def replace(n):
    n=str(n)
    n=n.replace('6','0')
    return n
    
inp=int(input())
print(replace(inp))
'''

def replace(n):
    n=str(n)
    n=n.replace('1','.')
    n=n.replace('2','1')
    n=n.replace('.','2')
    return n
    
inp=int(input())
print(replace(inp))
