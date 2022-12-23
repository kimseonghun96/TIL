dr = [-1, 1, 0, 0, -1, 1, 1, -1]
dc = [0, 0, -1, 1, -1, -1, 1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    ans = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'o':
                for k in range(8):
                    temp = 1
                    for t in range(1, 5):
                        nr, nc = r + dr[k] * t, c + dc[k] * t
                        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == '.':
                            temp = 1
                            break
                        elif 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 'o':
                            temp += 1
                    print(temp)
                    if temp == 5:
                        ans = temp
    # print(ans)

    if ans == 5:
        print(f'#{tc}', 'YES')
    else:
        print(f'#{tc}', 'NO')

