# 정상수

a, b = input().split()

a_num = int(a[::-1])
b_num = int(b[::-1])

if a_num > b_num:
    print(a_num)
else:
    print(b_num)