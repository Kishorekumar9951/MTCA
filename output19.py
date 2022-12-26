def extract_specialcharacters(s):
    temp_specialcharacters=''
    for i in s:
        if not i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789':
            temp_specialcharacters+=i
    return temp_specialcharacters
str1=input()
a=extract_specialcharacters(str1)
print("specialcharacters:",a)
    
