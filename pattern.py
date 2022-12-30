def printSeriesIncreasing(ch,n):
    assert isinstance(ch,str),"first arguement should be string"
    assert isinstance(n,int),'second argument should be int'
    for i in range(1,n+1):
        print(ch*i)
    return None

def printSeriesDecreasing(ch,n):
    for i in range(n,0,-1):
        print(ch*i)
    return None

inpCh=input("enter a character:")
inpNum=int(input("enter a no:"))
try:
    printSeriesIncreasing(inpCh,inpNum)
except AssertionError as ob:
    print(ob)
    print('-'*40)
printSeriesDecreasing(inpCh,inpNum)
