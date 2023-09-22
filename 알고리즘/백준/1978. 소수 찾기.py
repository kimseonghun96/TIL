# 특정 숫자 x가 소수인지 판별하는 가장 기본적인 알고리즘

def primenum(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


n = int(input())
num = list(map(int, input().split()))

cnt = 0
for i in range(n):
    if primenum(num[i]) == True and num[i] != 1:
        cnt += 1
    else:
        pass


print(cnt)