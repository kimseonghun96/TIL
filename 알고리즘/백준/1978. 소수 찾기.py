# 특정 숫자 x가 소수인지 판별하는 가장 기본적인 알고리즘
def primenumber(x):
    for i in range(2, x): # 2부터 x-1까지의 모든 숫자
        if x % i == 0:		# 나눠떨어지는게 하나라도 있으면 False
            return False
    return True				# 전부 나눠떨어지지 않으면 True


n = int(input())
arr = []
num = list(map(int, input().split()))
for i in range(n):
    if primenumber(num[i]) == True and num[i] != 1:
        arr.append(primenumber(num[i]))
    else:
        pass

print(len(arr))