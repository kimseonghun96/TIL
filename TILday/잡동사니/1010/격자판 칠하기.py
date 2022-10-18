# 물음표를 일단 바꾸고
'''
3
3 6
#.????
?#????
???.??
1 6
##????
3 3
.#.
#?#
.#.
'''

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    ans = 'possible'
    for r in range(N):
        for c in range(M):
            if arr[r][c] == '#':
                for k in range(4):
                    nr, nc = r + dr[k], c + dc[k]
                    if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == '?':
                        arr[nr][nc] = '.'

            if arr[r][c] == '.':
                for k in range(4):
                    nr, nc = r + dr[k], c + dc[k]
                    if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == '?':
                        arr[nr][nc] = '#'

    for i in range(N):
        for j in range(M):
            if arr[i][j] == '#':
                for k in range(4):
                    nr, nc = i + dr[k], j + dc[k]
                    if 0 <= nr < N and 0 <= nc < M:
                        if arr[nr][nc] == '#':
                            ans = 'impossible'

            if arr[i][j] == '.':
                for k in range(4):
                    nr, nc = i + dr[k], j + dc[k]
                    if 0 <= nr < N and 0 <= nc < M:
                        if arr[nr][nc] == '.':
                            ans = 'impossible'

    print(f'#{tc} {ans}')

