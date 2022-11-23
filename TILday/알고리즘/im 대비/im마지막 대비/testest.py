# 델타검색
# 돌을 놓은 위치에서 팔방탐색하여 다른 색을 찾는다.
# 다른 색을 찾는다면 그 방향으로 무슨 돌이 있는지 체크해준다.
# 가다가 0이 있다면 바로 break로 빠져 나오고, 같은 색을 찾는다면 그 앞에 다른 색을 다 같은색으로 바꿔준다.
# dr = [1, 0, -1, 0, 1, -1, -1, 1]
# dc = [0, 1, 0, -1, 1, 1, -1, -1]

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    othello = [[0] * (N + 1) for _ in range(N + 1)]
    othello[N // 2][N // 2], othello[N // 2 + 1][N // 2 + 1] = 2, 2
    othello[N // 2][N // 2 + 1], othello[N // 2 + 1][N // 2] = 1, 1

    for m in range(M):
        r, c, color = map(int, input().split())

        othello[r][c] = color
        for dir in range(8):
            nr1, nc1 = r + dr[dir] * 1, c + dc[dir] * 1
            for i in range(2, N + 1):
                nr2, nc2 = r + dr[dir] * i, c + dc[dir] * i
                if 1 <= nr1 < N + 1 and 1 <= nc1 < N + 1:
                    if othello[nr1][nc1] != color and othello[nr1][nc1] != 0:
                        if 1 <= nr2 < N + 1 and 1 <= nc2 < N + 1:
                            if othello[nr2][nc2] == 0:
                                break
                            if othello[nr2][nc2] == color:
                                for j in range(1, i):
                                    othello[r + dr[dir] * j][c + dc[dir] * j] = color
                                    continue

    cnt1 = 0
    cnt2 = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if othello[i][j] == 1:
                cnt1 += 1
            if othello[i][j] == 2:
                cnt2 += 1
    print(f'#{tc} {cnt1} {cnt2}')