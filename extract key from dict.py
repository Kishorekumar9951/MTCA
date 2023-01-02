sampledict={
    "name":"jasmine",
    "age": 22,
    "salary":80000,
    "city":"loveland"
    }
keys=["name","salary"]

##newDict={}
##for i in keys:
##    newDict=sampledict[i]
##print(newDict)

##newDict={ i:sampledict[i] for i in keys }
##print(newDict)
##
##res=dict()
##for k in keys:
##    res.update({k: sampledict[k]})
##print(res)

#keys to remove
##for k in keys:
##    sampledict.pop(k)
##print(sampledict)


##d=dict()
##for i in sampledict.keys()-keys:
##    d[i]=sampledict[i]
##print(d)

sampledict['location']=sampledict.pop('city')
print(sampledict)






