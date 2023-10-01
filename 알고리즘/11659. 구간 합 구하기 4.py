# 구간합을 알고리즘 많이 나옴..

import sys

N, M = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

prefix_sum = [0] * N

for k in range(1, len(arr)):
    prefix_sum[0] = arr[0]
    prefix_sum[k] = prefix_sum[k-1] + arr[k]


for t in range(M):
    i, j = map(int, sys.stdin.readline().split())
    if i == 1:
        ans = prefix_sum[j-1]
    elif i == j :
        ans = arr[i-1]
    else:
        ans = prefix_sum[j-1] - prefix_sum[i-2]

    print(ans)
