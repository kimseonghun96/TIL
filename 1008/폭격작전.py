'''
3
4 1
0 2 1 3
1 0 0 1
2 0 2 0
3 2 2 2
1 1 2
4 2
3 2 0 3
3 0 3 0
1 0 0 2
0 3 3 3
2 1 2
0 1 2
5 2
2 4 3 1 3
4 0 2 3 2
2 0 3 4 3
1 3 4 3 1
3 0 3 3 4
1 2 2
2 1 1
'''
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N, M= map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(M):
        r, c, boom = map(int, input().split())
        for i in range(N):
            for j in range(N):
                temp = arr[r][c]
                arr[r][c] = 0
                for k in range(4):
                    for t in range(1, boom+1):
                        nr, nc = r + dr[k] * t, c + dc[k] * t
                        if 0 <= nr < N and 0 <= nc < N:
                            temp += arr[nr][nc]
                            arr[nr][nc] = 0
                            ans += temp
                            temp = 0

    print(f'#{tc} {ans}')

