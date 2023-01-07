N = int(input())
dp = [0] * N
wine = []
for _ in range(N):
    wine.append(int(input()))

if N == 1: #잔이 1개일 때
    dp[0] = wine[0]

elif N == 2: #잔이 2개일 때
    dp[1] = wine[0] + wine[1]

elif N == 3: #잔이 3개일 때
    dp[2] = max(wine[0] + wine[1], wine[0] + wine[2], wine[1] + wine[2])

#잔이 4개일 때
else:
    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]
    dp[2] = max(wine[0] + wine[1], wine[0] + wine[2], wine[1] + wine[2])

    for i in range(3, N):
        dp[i] = max(dp[i-1], dp[i-2]+wine[i], dp[i-3]+wine[i-1]+wine[i])

print(dp[N-1])