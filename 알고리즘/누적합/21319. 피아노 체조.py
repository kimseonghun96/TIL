import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split())) +[11111111111]
t = int(input())
cnt = 0
dp = [0 for _ in range(n+1)]


for i in range(n):
    if arr[i] > arr[i+1]:
        dp[i+1] += cnt + 1
        cnt += 1
    else:
        dp[i+1] = cnt

for _ in range(t):
    x, y = map(int, input().split())
    print(dp[y-1] - dp[x-1])

# t = int(input())
# li = list(map(int, input().split()))
#
# res = [0] * t
# for i in range(len(li) - 1):
#     if li[i + 1] < li[i]:
#         res[i] = 1
#
# prefix_sum = [0] * (t + 1)
# for i in range(1, t + 1):
#     prefix_sum[i] = prefix_sum[i - 1] + res[i - 1]
#
# print(prefix_sum)
# for _ in range(int(input())):
#     i, j = map(int, input().split())
#     print(prefix_sum[j - 1] - prefix_sum[i - 1])