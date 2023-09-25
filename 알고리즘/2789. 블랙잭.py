import sys

input = sys.stdin.readline
n, m = map(int, input().split())

cards = list(map(int, input().split()))

ans = 0

for i in cards:
    for j in cards:
        for k in cards:
            if i != j and i != k and j != k:
                if i + j + k <= m and i + j + k > ans:
                    ans = i + j + k

print(ans)