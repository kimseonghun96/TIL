'''
4
5
....o
...o.
..o..
.o...
o....
5
...o.
ooooo
...o.
...o.
.....
5
.o.oo
oo.oo
.oo..
.o...
.o...
5
.o.o.
o.o.o
.o.o.
o.o.o
.o.o.
'''
dr = [-1, 1, 0, 0] # 십자가
dc = [0, 0, -1, 1 ]

gak_r = [-1, 1, 1, -1] # 대각
gak_c = [-1, -1, 1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    # print(board)

    ans = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == 'o':
                # cnt = 1
                for k in range(4):
                    cnt = 1
                    for t in range(1, 5):
                        nr, nc = r + dr[k] * t, c + dc[k] * t
                        if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 'o':
                            cnt += 1
                            if cnt == 5:
                                ans = cnt

    # print(ans)
    gak_ans = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == 'o':
                # cnt = 0
                for k in range(4):
                    cnt = 1
                    for t in range(1, 5):
                        nr, nc = r + gak_r[k] * t, c + gak_c[k] * t
                        if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 'o':
                            cnt += 1
                            if cnt == 5:
                                gak_ans = cnt

    # print(gak_ans)
    if gak_ans or ans == 5:
        print(f'#{tc}', 'YES')

    else:
        print(f'#{tc}', 'NO')

