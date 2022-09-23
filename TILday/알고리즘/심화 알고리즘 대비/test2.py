def dfs(dr, dc):
    global answer
    w, s = 0, 0  # 늑대와 양 수
    stack = [(dr, dc)]
    visit = set()

    while stack:
        current = stack.pop()
        r = current[0]
        c = current[1]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visit:
                # 벽 안에서
                if arr[nr][nc] != '#':
                    stack.append((arr[nr][nc]))
                    visit.add((arr[nr][nc]))
                    if arr[nr][nc] == 'o':
                        s += 1
                        arr[nr][nc] = '.'
                    if arr[nr][nc] == 'V':
                        w += 1
                        arr[nr][nc] = '.'
# [5] 영역 안에서 많은 애만 살아남는다. 적은 애는 죽었음
    if w >= s:
        answer[1] += w
    else:
        answer[0] += s
    return


R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
answer = [0, 0] # 양, 늑대
# 전체를 탐색하면서 양이나 늑대를 만나면 DFS로 들어간다.
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'o':
            dfs(i, j)
        elif arr[i][j] == 'v':
            dfs(i, j,)

print(*answer)