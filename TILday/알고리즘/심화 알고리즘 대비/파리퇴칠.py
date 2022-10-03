'''
1
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3
'''
dr = [-1, 0, 1, 0]  # 십자가
dc = [0, -1, 0, 1]

gak_r = [-1, -1, 1, 1]  # 대각
gak_c = [-1, 1, 1, -1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for r in range(N):
        for c in range(N):
            temp = arr[r][c]
            for i in range(4):
                for j in range(1, M):
                    nr, nc = r + dr[i]*j, c + dc[i]*j
                    if 0 <= nr < N and 0 <= nc < N:
                        temp += arr[nr][nc]
                        if ans < temp:
                            ans = temp

    for r in range(N):
        for c in range(N):
            temp = arr[r][c]
            for i in range(4):
                for j in range(1, M):
                    nr, nc = r + gak_r[i]*j, c + gak_c[i]*j
                    if 0 <= nr < N and 0 <= nc < N:
                        temp += arr[nr][nc]
                        if ans < temp:
                            ans = temp


    print(f'#{tc} {ans}')