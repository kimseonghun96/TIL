import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N+1)

#바텀업 방식
for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    # i값이 2, 3으로 나누어지지 않아서 1로 빼야하는 값
    print(dp)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    #i값이 2로 나누어 떨어지면,
    #위에서 1을 뺀 값이랑, 2로 나눠준 값에서 1을 더한 값 중에 작은 값을 택한다.
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[N])