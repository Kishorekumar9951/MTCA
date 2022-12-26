def count_digits(s):
    n_digits=0
    for i in s:
        if i in '0123456789':
            n_digits+=1
    return n_digits
str1=input()
a=count_digits(str1)
print("no of digits in:'",str1,"' is",a)
