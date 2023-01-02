##def printMonth(dn):
##    if dn==1:
##        return 'january'
##    elif dn==2:
##        return 'february'
##    elif dn==3:
##        return 'march'
##    elif dn==4:
##        return 'april'
##    elif dn==5:
##        return 'may'
##    elif dn==6:
##        return 'june'
##    elif dn==7:
##        return 'july'
##    elif dn==8:
##        return 'august'
##    elif dn==9:
##        return 'september'
##    elif dn==10:
##        return 'october'
##    elif dn==11:
##        return 'november'
##    elif dn==12:
##        return 'december'
##    else:
##        return 'None'
##
##for i in range(3):
##    inpNum=int(input())
##    print(printMonth(inpNum))


months={1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December',}
n=int(input())
for count in range(n):
    mn=int(input())
    if mn>=1 and mn<=12:
        print(months[mn])
    else:
        print("INVALID")




















    
