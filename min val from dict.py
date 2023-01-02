##sampledict={
##    'physics':85,
##    'math':66,
##    'history':45
##    }
##print(max(sampledict,key=sampledict.get))

sampledict={
    'emp1':{'name': 'jhon', 'salary':7500},
    'emp2':{'name': 'appu', 'salary':6500},
    'emp3':{'name': 'jasmine', 'salary':5500}
}
sampledict['emp3']['salary']=8500
print(sampledict)
