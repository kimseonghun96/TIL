# 최대 공약수를 구하는 함수 gcd를 선언
# 두 수 a, b를 받아서 b가 0이 될 때까지 a와 b를 나눈 나머지로 재귀적으로 gcd를 구한다
# b가 0이 되면 a가 최대 공약수.
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# 입력으로 두 개의 수 n과 m을 받아서 저장한다
n, m = map(int, input().split())

# gcd 함수를 이용해 최대 공약수를 구한다.
gcd_val = gcd(n, m)
# 최소 공배수는 (n * m) / gcd 로 구한다.
lcm_val = (n * m) // gcd_val

print(gcd_val)
print(lcm_val)

# n, m = map(int, input().split())
#
# arr = []
#
# arr.append(n)
# arr.append(m)
#
# min_ans = []
# max_ans = 0
#
# for i in range(1, max(arr)):
#     if n % i == 0 and m % i == 0:
#         min_ans.append(i)
#
#
# for i in range(max(arr), 999999):
#     if i % n == 0 and i % m == 0:
#         max_ans = i
#         break
#
# print(max(min_ans))
# print(max_ans)
