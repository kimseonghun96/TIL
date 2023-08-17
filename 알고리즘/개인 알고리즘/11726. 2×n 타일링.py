# 타일의 방법의 수를 구해야함
# 그 수를 10007로 나눈 나머지 출력
# n은 1 <= n <= 1000

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)

dp[0] = 1
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n]%10007)
