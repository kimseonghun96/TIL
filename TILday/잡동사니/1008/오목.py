import sys
sys.stdin = open('input.txt')

dr = [-1, 1, 0 , 0, -1, 1, 1, -1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input()*N for _ in range(N)]

    rc_cnt = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'o':
                for k in range(8):
                    cnt = 1
                    for t in range(1, N):
                        nr, nc = r + dr[k] * t, c + dc[k] * t
                        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 'o':
                            cnt += 1
                            if cnt == 5:
                                rc_cnt = cnt


    # print(rc_cnt)
    # print(gak_cnt)

    if rc_cnt == 5:
        ans = 'yes'
    else:
        ans = 'no'

    print(f'#{tc} {ans}')





# dr = [-1, 1, 0 , 0, -1, 1, 1, -1]
# dc = [0, 0, -1, 1, -1, 1, -1, 1]





