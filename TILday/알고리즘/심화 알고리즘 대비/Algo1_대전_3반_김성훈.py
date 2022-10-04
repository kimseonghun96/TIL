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
# 완전 탐색을 통해 2를 찾게 되면
# 델타를 사용해 1 전까지 숫자로 채움 --> 1 전까지를 못하겠습니다.
# 마지막 0의 개수 출력

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]


    ans = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                for k in range(4):
                    for t in range(1, N):
                        nr = r + dr[k] * t
                        nc = c + dc[k] * t
                        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 2 :
                            if arr[nr][nc] == 1:
                                break
                        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 2 and arr[nr][nc] != 1:
                            arr[nr][nc] = 3

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                ans += 1

    print(f'#{tc} {ans}')
