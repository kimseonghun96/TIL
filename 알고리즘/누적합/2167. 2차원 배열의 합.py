# n, m = map(int, input().split())
#
# arr = [list(map(int, input().split())) for _ in range(n)] # 가로를 기준으로 2차원 배열 받는 법
#
# count = int(input())
#
# for _ in range(count):
#     i, j, x, y = map(int, input().split())
#     ans = 0
#     for r in range(i-1, x):
#         for c in range(j-1, y):
#             ans += arr[r][c]
#
#     print(ans)
#
#
# --> 시간초과 dp를 사용해야함


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]  # 2차원 배열 받는 거는 가로로

count = int(input())  # 몇 번 할껀지

dp = [[0 for _ in range((m+1))] for _ in range(n+1)]  # 누적합 할 빈 리스트를 만들어 둠

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] + arr[i-1][j-1] - dp[i-1][j-1]

for _ in range(count):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])

