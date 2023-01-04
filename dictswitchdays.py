def printSunday():
    print('you chose sunday!\n')
def printMonday():
    print('you chose monday!\n')
def printTuesday():
    print('you chose tuesday!\n')
def printWednesday():
    print('you chose wednesday!\n')
def printThursday():
    print('you chose thursday!\n')
def printFriday():
    print('you chose friday!\n')
def printSaturday():
    print('you chose saturday!\n')
def choice():
    print("enter day number 1-7") 
Jasmine={1:printSunday,2:printMonday,3:printTuesday,4:printWednesday,5:printThursday,6:printFriday,7:printSaturday}
selection=0
while True:
    if selection ==8:break
    choice()
    selection=int(input("select a day option:"))
    if (selection>=0) and (selection<8):
        Jasmine[selection]()
