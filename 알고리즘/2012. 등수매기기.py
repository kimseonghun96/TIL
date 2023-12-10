import sys
input = sys.stdin.readline

n = int(input())

arr = []

for i in range(n):
    score = int(input())
    arr.append(score)

arr.sort()

ans = 0
for i in range(1, n+1):
    ans += abs(arr[i-1] - i)



print(ans)