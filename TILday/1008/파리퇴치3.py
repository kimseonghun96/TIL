'''
2
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3
6 3
29 21 26 9 5 8
21 19 8 0 21 19
9 24 2 11 4 24
19 29 1 0 21 19
10 29 6 18 4 3
29 11 15 3 3 29
'''
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

gak_r = [-1, -1, 1, 1]
gak_c = [-1, 1, 1, -1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for r in range(N):
        for c in range(N):
            temp = arr[r][c]
            for k in range(4):
                for t in range(1, M):
                    nr, nc = r +dr[k] * t, c + dc[k] * t
                    if 0 <= nr < N and 0 <= nc < N:
                        temp += arr[nr][nc]
                        if ans < temp:
                            ans = temp
    for r in range(N):
        for c in range(N):
            temp = arr[r][c]
            for k in range(4):
                for t in range(1, M):
                    nr, nc = r + gak_r[k] * t, c + gak_c[k] * t
                    if 0 <= nr < N and 0 <= nc < N:
                        temp += arr[nr][nc]
                        if ans < temp:
                            ans = temp

    print(f'#{tc} {ans}')
