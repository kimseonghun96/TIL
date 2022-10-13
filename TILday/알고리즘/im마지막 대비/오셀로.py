# import sys
# sys.stdin = open('input.txt')
# 돌을 놓는다.
# 그 돌 사방 탐색 해서 다른 색의 돌을 찾는다.
# 그 돌 대각이나, 십자가에 다른 색의 돌이 두 개 있으면 그 돌도 같은 색으로 바꿔 준다.
'''
1
4 12
1 2 1
1 1 2
4 3 1
4 4 2
2 1 1
4 2 2
3 4 1
1 3 2
2 4 1
1 4 2
4 1 2
3 1 2
'''
#
# dr = [-1, 1, 0, 0, -1, 1, -1, 1]
# dc = [0, 0, -1, 1, -1, 1, 1, -1]
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, play = map(int, input().split())
#     arr = [[0] * (N+1) for _ in range(N+1)]
#     middle = (N // 2)
#     arr[middle][middle] = 'W'
#     arr[middle][middle + 1] = 'B'
#     arr[middle + 1][middle] = 'B'
#     arr[middle + 1][middle + 1] = 'W'
#     # print(arr)
#
#     for i in range(play):
#         r, c, color = map(int, input().split())  # 1은 흑 2는 백
#         # 내가 지금 놓는 돌이 흑일 경우
#         if color == 1:
#             if 1 <= r < N+1 and 1 <= c < N+1:
#                 arr[r][c] = 'B'  # 일단 그자리에 흑을 놔
#
#                 for k in range(8):  # 그리고 팔방 탐색
#                     nr1, nc1 = r + dr[k] * 1, c + dc[k] * 1
#                     if 1 <= nr1 < N + 1 and 1 <= nc1 < N + 1:
#                         if arr[nr1][nc1] == 'W':
#                             for t in range(2, N+1):  # 쭉 갈 꺼
#                                 nr2, nc2 = r + dr[k] * t, c + dc[k] * t
#                                 if 1 <= nr2 < N+1 and 1 <= nc2 < N+1:  # 범위를 넘지 않고
#                                     if arr[nr2][nc2] == 'B' and arr[nr2][nc2] != 0:  # 움직인 곳에서 B를 찾아
#                                         for z in range(t):  # 움직인 거리안에서
#                                             if 1 <= r + dr[k] * z < N + 1 and 1 <= c + dc[k] * z < N + 1:
#                                                 if arr[r + dr[k] * z][c + dc[k] * z] == 'W':  # B가 있으면
#                                                     arr[r + dr[k] * z][c + dc[k] * z] = 'B'  # W로 바꿔줌
#
#                                             elif 1 <= r + dr[k] * z < N + 1 and 1 <= c + dc[z] * z < N + 1 and arr[r + dr[k] * z][c + dc[k] * z] == 'B':
#                                                 break
#
#
#         # print(arr)
#         # 내가 지금 놓는 돌이 백일 경우
#         if color == 2:
#             if 1 <= r < N+1 and 1 <= c < N+1:
#                 arr[r][c] = 'W'  # 일단 그자리에 흑을 놔
#
#                 for k in range(8):  # 그리고 팔방 탐색
#                     nr1, nc1 = r + dr[k] * 1, c + dc[k] * 1
#                     if 1 <= nr1 < N +1 and 1 <= nc1 < N+1:
#                         if arr[nr1][nc1] == 'B':
#                             for t in range(2, N + 1):  # 쭉 갈 꺼
#                                 nr2, nc2 = r + dr[k] * t, c + dc[k] * t
#                                 if 1 <= nr2 < N + 1 and 1 <= nc2 < N + 1:  # 범위를 넘지 않고
#                                     if arr[nr2][nc2] == 'W' and arr[nr2][nc2] != 0:  # 움직인 곳에서 B를 찾아
#                                         for z in range(t):  # 움직인 거리안에서
#                                             if 1 <= r + dr[k] * z < N + 1 and 1 <= c + dc[k] * z < N + 1:
#                                                 if arr[r + dr[k] * z][c + dc[k] * z] == 'B':  # B가 있으면
#                                                     arr[r + dr[k] * z][c + dc[k] * z] = 'W'  # W로 바꿔줌
#
#                                             elif 1 <= r + dr[k] * z < N + 1 and 1 <= c + dc[z] * z < N + 1 and arr[r + dr[k] * z][c + dc[k] * z] == 'W':
#                                                 break
#
#
#
#     # print(arr)
#     black = 0
#     white = 0
#     for i in range(1, N+1):
#         for j in range(1, N+1):
#             if arr[i][j] == 'B':
#                 black += 1
#             elif arr[i][j] == 'W':
#                 white += 1
#     # print(arr)
#     print(f'#{tc} {black} {white}')


# 델타검색
# 돌을 놓은 위치에서 팔방탐색하여 다른 색을 찾는다.
# 다른 색을 찾는다면 그 방향으로 무슨 돌이 있는지 체크해준다.
# 가다가 0이 있다면 바로 break로 빠져 나오고, 같은 색을 찾는다면 그 앞에 다른 색을 다 같은색으로 바꿔준다.
dr = [1, 0, -1, 0, 1, -1, -1, 1]
dc = [0, 1, 0, -1, 1, 1, -1, -1]

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [[0] * (N + 1) for _ in range(N + 1)]
    arr[N // 2][N // 2], arr[N // 2 + 1][N // 2 + 1] = 2, 2
    arr[N // 2][N // 2 + 1], arr[N // 2 + 1][N // 2] = 1, 1

    for m in range(M):
        r, c, color = map(int, input().split())

        arr[r][c] = color
        for k in range(8):
            nr1, nc1 = r + dr[k], c + dc[k]

            for i in range(2, N + 1):
                nr2, nc2 = r + dr[k] * i, c + dc[k] * i

                if 1 <= nr1 < N + 1 and 1 <= nc1 < N + 1:
                    if arr[nr1][nc1] != color and arr[nr1][nc1] != 0:
                        if 1 <= nr2 < N + 1 and 1 <= nc2 < N + 1:
                            if arr[nr2][nc2] == 0:
                                break

                            if arr[nr2][nc2] == color:
                                for j in range(1, i):
                                    arr[r + dr[k] * j][c + dc[k] * j] = color
                                    continue

    black = 0
    white = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if arr[i][j] == 1:
                black += 1
            if arr[i][j] == 2:
                white += 1
    print(f'#{tc} {black} {white}')
