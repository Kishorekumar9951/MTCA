def extract_consonants(s):
    temp_consonants=''
    for i in s:
        #print("i=",i)
        if i  in 'BCDGHJKLMNPQRSTVWXYZbcdhjklmnpqrstvwxyz':
            temp_consonants+=i
            #print("i:",i,"temp_consonants:",temp_consonants)
    return temp_consonants
str1=input()
a=extract_consonants(str1)
print("consonants:",a)
    
