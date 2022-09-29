# 델타를 사용한다 수직 수평
# 기준점에 따라 그 구간의 합을 각각 구하고 겹치는 부분이 있을 수 있기 때문에
# 먼저 합을 구한 곳은 0으로 바꿔준다.
# 다 더한다.
'''
1
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
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    result = 0
    for i in range(M):
        r, c, boom = map(int, input().split())
        start = arr[r][c]
        for x in range(N):
            for y in range(N):
                # print(start)
                for k in range(boom+1):
                    for dir in range(4):
                        nr, nc = r+dr[dir]*k, c + dc[dir]*k
                        if 0 <= nr < N and 0 <= nc < N:
                            ans += arr[nr][nc]
                            arr[nr][nc] = 0
    print(f'#{tc} {ans}')



