# 먼저 '2' 라는 시작점을 stack에 저장한다.
# dfs 처럼 stack에 담긴 좌표를 하나씩 꺼내가며 3을 찾아간다.
# 내가 보고 있는 좌표가 0일 경우엔 stack과 visited에 담아가며
# 3을 찾아간다.

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    ans = 0   # 결과의 초기값

    start = (0, 0)      # 시작점을 찾기위해 초기값 설정
    for r in range(N):
        for c in range(N):
            if arr[r][c] == '2':
                start = (r, c)          # 2가 있는 곳이 시작 지점이 된다.

    stack = [start, ]                   # 스택에 시작 점을 담는다.
    visited = set()                     # 방문 기록 할 곳

    while stack:                            # 스택이 빌 때까지 돌아라, 좌표 설정
        pick = stack.pop()
        x = pick[0]                         # 좌표 설정
        y = pick[1]
        for k in range(4):                      # 내가 보고 있는 곳에서 상하좌우 둘러 본다.
            nr, nc = x + dr[k], y + dc[k]
            if 0 <= nr < N and  0 <= nc < N and (nr, nc) not in visited:    # 내가 보는 곳이 범위가 벗어나지 않고 방문도 하지 않았는데
                if arr[nr][nc] == '3':          # 3이라면 도착지점이 있는 것이니까
                    ans = 1                     # 결과를 미로를 찾았다고 바꾸고
                    break                       # 종료한다.

                elif arr[nr][nc] == '0':        # 내가 간 곳이 0이라면
                    stack.append((nr, nc))      # 스택에 좌표 추가
                    visited.add((nr, nc))       # 방문기록에도 기록해준다.

    print(f'#{tc} {ans}')
