N = 7
arr =[[0]* N for _ in range(N)]

dr = [-1, 0, 1, 0]  # 상 우 하 좌
dc = [0, 1, 0, -1]

# dr = [-1, -1, 1, 1]  # 상 우 하 좌
# dc = [-1, 1, 1, -1]

r, c = 2, 2    # 기준점
arr[r][c] = '*'

nr, nc = r, c
for _ in range(1, N):
    nr, nc = nr + dr[1], nc + dc[1]
    if not(0 <= nr < N and 0 <= nc < N):
        break
    arr[nr][nc] = 1

while 0 <= nr + dr[1] < N and 0 <= nc + dc[1] < N:
    nr, nc = nr + dr[1], nc + dc[1]
    arr[nr][nc] = 1


#네 방향에 대해서 해보자
# for dir in range(4):
#     for i in range(1, N):
#         nr, nc = r + dr[dir]*i, c + dc[dir]*i
#         if 0 <= nr < N and 0 <= nc < N:
#             arr[nr][nc] = dir + 1



# for dir in range(4):
#     nr, nc = r + dr[dir], c + dc[dir]
#     if 0 <= nr < N and 0 <= nc < N:
#         arr[nr][nc] = dir + 1

for line in arr:
    print(*line)
