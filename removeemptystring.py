##for i in range(5):
##    inp=input()
##    if inp:
##        print("Hello "+inp)
##    else:
##        print("Bye "+inp)

lst=["Sedan", "SUV", "", "", "Pickup",'', ' ']
ans=[]
for i in lst:
    if i:
        ans.append(i)
print(ans)
