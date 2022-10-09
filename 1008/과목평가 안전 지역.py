'''
3
5
0 1 0 0 0
0 0 2 2 0
0 1 0 0 0
0 2 1 2 0
0 0 0 0 0
5
0 0 0 0 0
0 2 1 2 0
0 1 0 1 0
0 2 1 2 0
0 0 0 0 0
5
0 0 1 0 0
1 2 0 1 0
0 1 2 0 1
1 0 0 2 0
0 1 2 0 1
'''
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     ans = 0
#     for r in range(N):
#         for c in range(N):
#             if arr[r][c] == 2:
#                 for k in range(4):
#                     for t in range(1, N):
#                         nr, nc = r + dr[k] * t, c + dc[k] * t
#                         if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1 and arr[nr][nc] != 2:
#                             break
#                         elif 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
#                             arr[nr][nc] = 3
#     print(arr)
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 0:
#                 ans += 1
#
#     print(f'#{tc} {ans}')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                for k in range(4):
                    for t in range(1, N):
                        nr, nc = r + dr[k] * t, c + dc[k] * t
                        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
                            arr[nr][nc] = 3
                        elif 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1:
                            break

    print(arr)
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                ans += 1

    print(f'#{tc} {ans}')