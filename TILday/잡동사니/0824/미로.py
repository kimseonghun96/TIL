# def dfs(i, j, N):
#     global answer
#     if maze[i][j] == 3:
#         answer += 1
#         return
#     else:
#         visited[i][j] = 1
#         for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
#             ni, nj = i+di, j+dj
#             if maze[ni][nj] != 1 and visited[ni][nj] == 0: #벽으로 둘러쌓인 미로
#                 dfs(ni, nj, N)
#         visited[i][j] = 0            # 다른 경로로 갔던 곳 갈때도 횟수를 추가하기 위해
#         return
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     maze = [list(map(int, input())) for _ in range(N)]
#     sti = -1
#     stj = -1
#     for i in range(N):
#         for j in range(N):
#             if maze[i][j] == 2:
#                 sti, stj = i, j
#                 break
#         if sti != -1:
#             break
#     answer = 0          # 경로의 수
#     visited = [[0]*N for _ in range(N)]
#     dfs(sti, stj, N)
#     print(answer)

T = int(input())

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]     #lsit 안에 리스트lsit
    visited = set()  # 좌표 visited set
    answer = 0  # 안된다고 일단 먼저 생각

    initial_r = None
    initial_c = None
    for i in range(N):  # 최초 좌표를 찾기위한 코드
        flag = False

        for j in range(N):
            if maze[i][j] == 2:
                initial_r = i
                initial_c = j
                flag = True
                break

        if flag:
            break

    stack = [(initial_r, initial_c)]  # 최초 좌표를 tuple 형태로 넣음

    while stack:  # 빌때까지 돌아라!
        r, c = stack.pop()
        visited.add((r, c))  # set 특성상 중복제거 가능

        if maze[r][c] == 3:
            answer = 1
            break

        for d in range(4):  # 4방탐색
            nr = r + dr[d]
            nc = c + dc[d]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:  # 맵 벗어났다면?
                continue

            if maze[nr][nc] == 1 or (nr, nc) in visited:  # 벽이거나 간 곳이라면?
                continue

            stack.append((nr, nc))  # 살아남은 경우에만 append!

    print('#{} {}'.format(tc, answer))
