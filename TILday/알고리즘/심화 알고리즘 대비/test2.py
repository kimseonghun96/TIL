dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]



def dfs(r, c):
    global cnt
    if 0 <= r < N and 0 <= c < N and arr[r][c] == '1' and not visit[r][c]:
        cnt += 1
        arr[r][c] = 0
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            dfs(nr, nc)
        return 1
    return 0

N = int(input())
arr = [list(input()) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
cnt = 0
ans = []

for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            ans.append(cnt)
            cnt = 0

ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])

