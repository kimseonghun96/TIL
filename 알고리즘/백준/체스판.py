import copy
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
new_arr = copy.deepcopy(arr)
ans = []

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for r in range(N-7):
    for c in range(M-7):
        arr = new_arr
        count = 0
        for i in range(r, r+8):
            for j in range(c, c+8):
                if arr[i][j] == 'B':
                    for k in range(4):
                        nr, nc = i + dr[k], j +dc[k]
                        if r <= nr < r+8 and c <= nc < c+8:
                            if arr[nr][nc] != 'W':
                                arr[nr][nc] = 'W'
                                count += 1

                elif arr[i][j] == 'W':
                    for k in range(4):
                        nr, nc = i + dr[k], j + dc[k]
                        if r <= nr < r + 8 and c <= nc < c + 8:
                            if arr[nr][nc] != 'B':
                                arr[nr][nc] = 'B'
                                count += 1
            ans.append(count)

for line in arr:
    print(*line)

print()
for line in new_arr:
    print(*line)
print(ans)