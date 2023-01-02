##employees=["jasmine","appu"]
##defaults={"designation": "developer", "salary":80000}
##data=dict()
##for i in employees:
##    data[i]=defaults
##print(data)

employees=["jasmine","appu"]
defaults={"designation": "developer", "salary":80000}
data=dict.fromkeys(employees,defaults)

print(data["jasmine"])
