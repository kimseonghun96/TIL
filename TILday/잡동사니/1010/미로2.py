dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = 10
for tc in range(1, T+1):
    testcase = int(input())
    arr = [list(input()) for _ in range(100)]

    start = (0, 0)
    for r in range(100):
        for c in range(100):
            if arr[r][c] == '2':
                start = (r, c)

    stack = [start, ]
    visited = set()
    ans = 0

    while stack:
        pick = stack.pop()
        x = pick[0]
        y = pick[1]
        for k in range(4):
            nr, nc = x + dr[k], y + dc[k]
            if 0 <= nr < 100 and 0 <= nc < 100 and arr[nr][nc] == '3' and (nr, nc) not in visited:
                ans = 1
                break
            elif arr[nr][nc] == '0':
                stack.append((nr, nc))
                visited.add((nr, nc))

    print(ans)