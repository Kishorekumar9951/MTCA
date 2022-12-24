def primenumber(num):
    if num<1:
        return 0
    if num==1 or num==2 or num==3:
        return num
    for i in range(2,num):
        if num%i==0:
            return 0
    return num
lst=[]
first=int(input("enter the first num:"))
last=int(input("enter the last num:"))
for i in range(first,last+1):
    if primenumber(i):
        lst.append(i)
print(*lst)
print(len(lst))
    
