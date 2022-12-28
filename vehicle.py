dict1={"sedan":1500,"SUV":2000,"pickup":2500, "Van":2400, "Semi":13600, "Bicycle": 7, "Motorcycle": 110}
##ans=[]
##for i in dict1:
##    if dict1[i]<5000:
##        ans.append(i.upper())
##print(ans)


ans=[i.upper() for i in dict1 if dict1[i]<5000]
print(ans)
