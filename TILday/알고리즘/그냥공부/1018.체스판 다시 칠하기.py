import copy
'''
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
'''
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
arr2 = copy.deepcopy(arr)

cnt = []

for i in range(M-7):
    arr2 = arr
    test = 0
    for j in range(N-7):
        for r in range(i, i+8):
            for c in range(j, j+8):

                if arr2[r][c] == 'W':
                    for d in range(4):
                        for t in range(1,2):
                            nr, nc = r + dr[d]*t, c + dc[d]*t
                            if 0 <= nr < 8 and 0 <= nc < 8:
                                if arr2[nr][nc] == 'W':
                                    arr2[nr][nc] = 'B'
                                    test += 1

                if arr2[r][c] == 'B':
                    for d in range(4):
                        for t in range(1,2):
                            nr, nc = r + dr[d]*t, c + dc[d]*t
                            if 0 <= nr < M and 0 <= nc < N:
                                if arr2[nr][nc] == 'B':
                                    arr2[nr][nc] = 'W'
                                    test += 1

    cnt.append(test)


# for line in arr:
#     print(*line)

print(cnt)
