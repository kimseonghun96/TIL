'''
2
3
4
'''
dr = [0, 1, 0, -1]      #   하   상
dc = [1, 0, -1, 0]      # 우   좌

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    turn = 0
    r, c= 0, -1
    num = 1
    while num <= N*N:
        r, c = r + dr[turn], c + dc[turn]
        if 0 <= r < N and 0 <= c < N and arr[r][c] == 0:
            arr[r][c] = num
            num += 1

        else:
            r, c = r - dr[turn], c - dc[turn]
            turn = (turn+1) % 4

    for line in arr:
        print(*line)

