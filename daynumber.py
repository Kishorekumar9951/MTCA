def printDay(dn):
        if(dn==0):
            return 'sunday'
        elif (dn==1):
            return 'monday'
        elif (dn==2):
            return 'tuesday'
        elif (dn==3):
            return 'wednesday'
        elif (dn==4):
            return 'thursday'
        elif (dn==5):
            return 'friday'
        elif (dn==6):
            return 'saturday'
        else:
            return 'Invalid'
def printDay1(dn):
        if(dn==0):
            return 'sunday'
        if (dn==1):
            return 'monday'
        if (dn==2):
            return 'tuesday'
        if (dn==3):
            return 'wednesday'
        if (dn==4):
            return 'thursday'
        if (dn==5):
            return 'friday'
        if (dn==6):
            return 'saturday'
        else:
            return 'Invalid'
import time
for i in range(6):
    inpNum=int(input())
    start=time.time()
    print(printDay(inpNum))
    print(time.time()-start)
    start=time.time()
    print(printDay1(inpNum))
    print(time.time()-start)



    
