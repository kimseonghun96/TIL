# + 모양
dr1 = [-1, 0, 1, 0]  # 상 우 하 좌
dc1 = [0, 1, 0, -1]

# x 모양
dr2 = [-1, -1, 1, 1]  # 상 우 하 좌
dc2 = [-1, 1, 1, -1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr =[list(map(int, input().split())) for _ in range(N)]
    ans = 0

    # + 모양
    for r in range(N):
        for c in range(N):
            # 기준점 r, c
            kill = arr[r][c]  # 기준점은 한번만
            for dir in range(4):
                for i in range(1, M):   # 기준점 제외하고 다음 칸부터
                    nr, nc = r + dr1[dir] * i, c + dc1[dir] * i
                    if 0 <= nr < N and 0 <= nc < N:
                        kill += arr[nr][nc]
            ans = max(ans, kill)  # ans 는 kill 중에 가장 큰 것?

    #  x 모양
    for r in range(N):
        for c in range(N):
            # 기준점 r, c
            kill = arr[r][c]  # 기준점은 한번만
            for dir in range(4):
                for i in range(1, M):   # 기준점 제외하고 다음 칸부터
                    nr, nc = r + dr2[dir] * i, c + dc2[dir] * i
                    if 0 <= nr < N and 0 <= nc < N:
                        kill += arr[nr][nc]
            ans = max(ans, kill)


    print(f'#{tc} {ans}')
