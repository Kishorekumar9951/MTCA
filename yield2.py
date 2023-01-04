def Series(a,b):
    assert(a<b),"first arguement should be smaller than second."
    total=0
    for i in range(a,b,1):
        total=total+i
        yield total
n1=int(input())
n2=int(input())
ob=Series(n1,n2)
x=0
try:
    while x<10:
        print(next(ob))
        x=x+1
except AssertionError as ae:
    print(ae)
