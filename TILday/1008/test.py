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
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '#':   # 내가 찾은게 # 일 때
                for k in range(4):
                    nr, nc = i + dr[k], j + dc[k]
                    if 0 <= nr < N and 0 <= nc < N:
                        if arr[nr][nc] == '#':
                            ans = 'impossible'
                            break

            if arr[i][j] == '.':   # 내가 찾은게 . 일 때
                for k in range(4):
                    nr, nc = i + dr[k], j + dc[k]
                    if 0 <= nr < N and 0 <= nc < N:
                        if arr[nr][nc] == '.':
                            ans = 'impossible'
                            break

            if arr[i][j] == '?':  # 내가 찾은 점이 ? 일 때
                for k in range(4):
                    nr, nc = i + dr[k], j + dc[k]
                    if 0 <= nr < N and 0 <= nc < N:
                        if arr[nr][nc] == '.' and '#':
                            break

    print(f'#{tc} {ans}')