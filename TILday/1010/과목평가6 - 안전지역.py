'''
3
5
0 1 0 0 0
0 0 2 2 0
0 1 0 0 0
0 2 1 2 0
0 0 0 0 0
5
0 0 0 0 0
0 2 1 2 0
0 1 0 1 0
0 2 1 2 0
0 0 0 0 0
5
0 0 1 0 0
1 2 0 1 0
0 1 2 0 1
1 0 0 2 0
0 1 2 0 1
'''

# 탐색을 하다가 2를 만나면
# 델타 상하좌우 3을 찍다가
# 1을 만나면 브레이크

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N =int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0    # 나중에 안전지역의 개수를 파악할 곳

    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:   # 찾은 값이 2라면
                for k in range(4):
                    for t in range(1, N):
                        nr = r + dr[k] * t
                        nc = c + dc[k] * t
                        if 0 <= nr < N and 0 <= nc < N  and arr[nr][nc] == 1:   # 1일때ㅔ break
                            break

                        elif 0 <= nr < N and 0 <= nc < N  and arr[nr][nc] == 0:  # 0이면 3을 찍음
                            arr[nr][nc] = 3
    #
    # print(arr)
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                ans += 1


    print(f'#{tc} {ans}')



















