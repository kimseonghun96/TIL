arr = [[0]*100 for _ in range(100)]

cnt = 0
for i in range(4):
    r, c, r2, c2 = map(int, input().split())
    for i in range(r, r2):
        for j in range(c, c2):
            arr[i][j] = 1


for x in range(100):
    for y in range(100):
        if arr[x][y] == 1:
            cnt += 1

# for line in arr:
#     print(*line)
print(cnt)

