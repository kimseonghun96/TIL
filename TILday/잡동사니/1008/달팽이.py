# import sys
# sys.stdin = open('input.txt')

dr = [0, 1,  0, -1]
dc = [-1,0, 1, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    r, c = 0, 3
    d = 0

    for i in range(1, N*N+1):
    # while num <= N*N:
        r, c = r + dr[d], c + dc[d]
        if 0 <= r < N and 0 <= c < N and arr[r][c] == 0:
            arr[r][c] = i
            i += 1

        else:
            r, c = r - dr[d], c - dc[d]
            d = (1+d) % 4
            r, c = r + dr[d], c + dc[d]
            arr[r][c] = i
            i += 1

    print(f'#{tc}')
    for line in arr:
        print(*line)


