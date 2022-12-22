import sys
sys.stdin = open('input.txt')

dr = [0, 1]
dc = [1, 0]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    ans = 'yes'

    cnt = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == '#':
                for k in range(2):
                    nr, nc = r + dr[k] , r + dc[k]
                    if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == '.':
                        break

                for k in range(2):
                    nr, nc = r + dr[k] - 1  , r + dc[k] - 1
                    if 0 <= nr < N and 0 <= nc  < N and arr[nr][nc] == '#':
                        cnt += 1
                        # arr[nr][nc] = 0
                        r, c = nr, nc


    ans_cnt = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == '#':
                for i in range(r, r+(cnt//2 + cnt % 2)):
                    for j in range(c, c+(cnt//2 + cnt % 2)):
                        if arr[i][j] == '#':
                            ans_cnt += 1
                            arr[i][j] = 0

    if ans_cnt == 0 or ans_cnt != ((cnt//2 + cnt % 2)+1)**2:
        ans = 'no'

    print(f'#{tc} {ans}')


