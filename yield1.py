def sum(k):
    res=0
    for i in range(k+1):
        res=res+i
        yield("i=",i,"res=",res)
    return res
ob=sum(10)
for i in range(11):
    print(next(ob))
 
