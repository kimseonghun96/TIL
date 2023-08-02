import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

arr_sum = [0] * (N + 1)
for i in range(1, N + 1):
    arr_sum[i] = arr_sum[i - 1] + arr[i - 1]


ans = []

for i in range(N - K + 1):
    ans_sum = arr_sum[i + K] - arr_sum[i]
    ans.append(ans_sum)


print(max(ans))
