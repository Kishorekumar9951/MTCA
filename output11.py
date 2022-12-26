def checkPalindrome(s):
    if s==s[::-1]:
        return 'yes'
    else:
        return 'no'
inp=input()
print(checkPalindrome(inp))
