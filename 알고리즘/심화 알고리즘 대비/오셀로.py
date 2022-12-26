# import sys
# sys.stdin = open('input.txt')
# 돌을 놓는다.
# 그 돌 사방 탐색 해서 다른 색의 돌을 찾는다.
# 그 돌 대각이나, 십자가에 다른 색의 돌이 두 개 있으면 그 돌도 같은 색으로 바꿔 준다.


dr = [-1, 1, 0, 0, -1, 1, -1, 1]
dc = [0, 0, -1, 1, -1, 1, 1, -1]



T = int(input())
for tc in range(1, T+1):
    N, play = map(int, input().split())
    arr = [[0]*N for _ in range(N)]
    middle = (N//2) -1
    arr[middle][middle] = 'W'
    arr[middle][middle+1] = 'B'
    arr[middle+1][middle] = 'B'
    arr[middle+1][middle+1] = 'W'
    # print(arr)

    for i in range(play):
        r, c, color = map(int, input().split())  # 1은 흑 2는 백
        r = r - 1
        c = c - 1
        # 내가 지금 놓는 돌이 흑일 경우
        if color == 1:
            if 0 <= r < N and 0 <= c < N:
                arr[r][c] = 'B'             # 일단 그자리에 흑을 놔

                for k in range(8):          # 그리고 팔방 탐색
                    for t in range(1, N):   # 쭉 갈 꺼
                        nr, nc = r + dr[k] * t, c + dc[k] * t
                        if 0 <= nr < N and 0 <= nc < N: # 범위를 넘지 않고
                            if arr[nr][nc] == 'B':          # 움직인 곳에서 B를 찾아
                                for z in range(t):          # 움직인 거리안에서
                                    if 0 <= r + dr[k] * z < N and 0 <= c +dc[z] *z < N:
                                        if arr[r + dr[k] * z][c + dc[k] * z] == 'W':  # B가 있으면
                                            arr[r + dr[k] * z][c + dc[k] * z] = 'B'  # W로 바꿔줌

                            elif arr[nr][nc] == 0:
                                break
    # print(arr)
        # 내가 지금 놓는 돌이 백일 경우
        if color == 2:
            if 0 <= r < N and 0 <= c < N:
                arr[r][c] = 'W'             # 일단 그자리에 백을 놔

                for k in range(8):          # 그리고 팔방 탐색
                    for t in range(1, N):   # 쭉 갈 꺼
                        nr, nc = r + dr[k] * t, c + dc[k] * t
                        if 0 <= nr < N and 0 <= nc < N: # 범위를 넘지 않고
                            if arr[nr][nc] == 'W':          # 움직인 곳에서 W를 찾아
                                for z in range(t):          # 움직인 거리안에서
                                    if 0 <= r + dr[k] * z < N and 0 <= c + dc[k] * z < N:
                                        if arr[r+dr[k] * z][c+dc[k] * z] == 'B':        # B가 있으면
                                            arr[r + dr[k] * z][c + dc[k]*z] = 'W'     # W로 바꿔줌

                            elif arr[nr][nc] == 0:
                                break
    # print(arr)
    black = 0
    white = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'B':
                black += 1
            elif arr[i][j] == 'W':
                white += 1

    print(f'#{tc} {black} {white}')



