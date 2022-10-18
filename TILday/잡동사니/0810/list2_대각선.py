# 오른쪽 아래로 가는 대각선
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

s = 0
for i in range(N):
    for j in range(N):
        if i == j:
            s += arr[i][j]


s = 0
for i in range(N):
    s += arr[i][i]


#왼쪽 아래로 가는 대각선
s = 0
for i in range(N):
    s += arr[i][j-1-i]