dr = [0, 1, 0, -1] # 우 하 좌 상
dc = [1, 0, -1, 0]
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]

N = 5
arr = [[0] * N for _ in range(N)]

r, c = 0, -1
num = 1
dir = 0
while num <= N*N:
    r, c = r + dr[dir], c + dc[dir]
    if 0 <= r < N and 0 <= c < N and arr[r][c] == 0:
        arr[r][c] = num
        num += 1
    else:
        r, c = r - dr[dir], c - dc[dir]
        dir = (dir + 1) % 4


# while True:
#     r, c = r + dr[1], c + dc[1]
#     if 0 <= r < N and 0 <= c < N:
#         arr[r][c] = 2
#     else:
#
#         break
for line in arr:
    print(*line)