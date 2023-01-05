T = int(input())
dp = [0] * 11     #11보다 작은 수
for _ in range(T):
    n = int(input())

    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, 11):
        dp[i] = dp[i-1] + dp[i-2] +dp[i-3]

    print(dp[n])