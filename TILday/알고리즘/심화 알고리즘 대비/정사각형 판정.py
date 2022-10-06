import sys
sys.stdin = open('input.txt')
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    r_cnt = 0
    c_cnt = 0
    ans = 0
    for r in range(N):
        for c in range(N):
            # if arr.count('#') >= 2:
            if arr[r][c] == '#':
                for k in range(4):
                    for t in range(1, N):
                        nr, nc = r + dr[k] * t, c + dc[k] * t
                        if 0 <= nr < N and 0 <= nc < N:

                            if arr[nr][nc] == '.':
                                break
                            cnt = 0
                            if arr[nr][nc] == '#':
                                cnt +=1
                                ans += 1

    # print(arr)

            # if arr.count('#') == 1:
            #     print(f'#{tc}', 'yes')
    print(ans)
