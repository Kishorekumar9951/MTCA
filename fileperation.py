fo=open(r"D:\pythonpractice27\day9\notepad.txt","a")
for i in range(5):
    inpStr=input('Enter String:')
    fo.write(inpStr+'\n')
fo.close()
print(' Written to file')
