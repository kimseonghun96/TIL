import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    arr[i] = arr[i] + arr[i-1]

ans = 0
for i in range(n):
    if arr[i] == m:
        ans += 1
    else:
        for j in range(n):
            if arr[i] - arr[j] == m:
                ans += 1

print(ans)
