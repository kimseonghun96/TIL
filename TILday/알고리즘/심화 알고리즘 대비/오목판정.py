'''
1
5
....o
...o.
..o..
.....
.....
'''
dr = [-1, 1, 0, 0] # 십자가
dc = [0, 0 -1, 1 ]

gak_r = [-1, 1, 1, -1] # 대각
gak_c = [-1, -1, 1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(input()) for _ in range(N)]

    result = []
    for x in range(N):
        for y in range(N):
            if board[x][y] == 'o':
                r = x
                c = y
                cnt = 1
                gak_cnt = 1
                for t in range(4):
                    nr, nc = r + dr[t], c + dc[t]
                    if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 'o':
                        cnt += 1

                    print(cnt)
                    # for k in range(1, 3):
                    #     nr, nc = r + gak_r[k]*t, c + gak_c[k]*t
                    #     if 0 <= nr < N and 0 <= nc < N :
                    #         if board[nr][nc] == 'o':
                    #             gak_cnt += 1
    #             print(cnt)
    #             if gak_cnt or cnt == 5:
    #                 result = ('YES')
    #             else:
    #                 result.append(6)
    #
    # print(result)