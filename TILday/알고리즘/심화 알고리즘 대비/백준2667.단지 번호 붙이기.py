# 뭔가 dfs로 풀어야 할 듯하다.
# arr 을 돌면서 1을 만나면 1 속으로 들어가서 1이 있는 곳만 감
# 더이상 1을 통해 갈 수 없을 경우
# cnt += 1 해주고 그 값을 ans에 append
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c):
    global cnt
    if 0 <= r < N and 0 <= c < N and arr[r][c] == '1' and not visit[r][c]:
        cnt += 1
        arr[r][c] = 0
        for k in range(4):
            nr = r + dc[k]
            nc = c + dr[k]
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
# print(ans)
ans.sort()

print(len(ans))
for i in range(len(ans)):
    print(ans[i])


