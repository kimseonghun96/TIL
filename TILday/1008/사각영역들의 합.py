T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(M):
        r, c, line = map(int, input().split())
        ans += arr[r][c]
        arr[r][c] = 0
        for k in range(line):
            for t in range(line):
                nr = r + k
                nc = c + t
                if 0 <= nr < N and 0 <= nc < N:
                    ans += arr[nr][nc]
                    arr[nr][nc] = 0

    print(f'#{tc} {ans}')


