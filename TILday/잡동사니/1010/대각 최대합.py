'''
3
4
1 2 0 1
2 1 0 1
1 2 3 2
3 2 2 3
4
3 2 3 0
0 2 2 0
2 3 2 2
2 1 2 1
5
2 4 3 1 3
4 0 2 0 2
2 0 3 4 3
1 1 4 0 1
3 0 3 3 4
'''

gak_r = [-1, 1, 1, -1]
gak_c = [-1, -1, 1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for r in range(N):
        for c in range(N):
            temp = 0
            if arr[r][c]:
                temp += arr[r][c]
                for k in range(4):
                    for t in range(1, N):
                        nr , nc = r + gak_r[k] * t, c + gak_c[k] * t
                        if 0 <= nr < N and 0 <= nc < N:
                            temp += arr[nr][nc]
                            if ans <  temp:
                                ans = temp

    print(f'#{tc} {ans}')