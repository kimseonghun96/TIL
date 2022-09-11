str = list(input())
num = str.count(' ')
if str[0] == ' ':
    num -= 1
if str[-1] == ' ':
    num -= 1

print(num+1)