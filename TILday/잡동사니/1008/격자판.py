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
                    if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == '?':
                        arr[nr][nc] = '.'

            if arr[i][j] == '.':   # 내가 찾은게 . 일 때
                for k in range(4):
                    nr, nc = i + dr[k], j + dc[k]
                    if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == '?':
                        arr[nr][nc] = '#'
    # print(arr)
    for r in range(N):
        for c in range(M):
            if arr[r][c] == '#':
                for k in range(4):
                    nr, nc = r + dr[k], c + dc[k]
                    if 0 <= nr < N and 0 <= nc < M:
                        if arr[nr][nc] == '#':
                            ans = 'impossible'
            if arr[r][c] == '.':
                for k in range(4):
                    nr, nc = r + dr[k], c + dc[k]
                    if 0 <= nr < N and 0 <= nc < M:
                        if arr[nr][nc] == '.':
                            ans = 'impossible'

    print(f'#{tc} {ans}')




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
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(input()) for _ in range(N)]
#
#     ans = 'possible'
#     r, c = 0, 0
#     for i in range(N):
#         for j in range(M):
#             if arr[r][c] == '#':  # 시작점이 # 일 때
#                 for k in range(4):
#                     nr, nc = r + dr[k], c + dc[k]
#                     if 0 <= nr < N and 0 <= nc < M:
#                         if arr[nr][nc] == '#':
#                             ans = 'impossible'
#                             break
#
#                         elif arr[nr][nc] == '?' or '.':
#                             for t in range(4):
#                                 if 0 <= nr+dr[t] < N and 0 <= nc+dc[t] < M:
#                                     if arr[nr+dr[t]][nc+dc[t]] == '#' or '?':
#                                         pass
#                                     else:
#                                         ans = 'impossible'
#                                         break
#
#             if arr[r][c] == '.':  # 시작점이 . 일 때
#                 for k in range(4):
#                     nr, nc = r + dr[k], c + dc[k]
#                     if 0 <= nr < N and 0 <= nc < M:
#                         if arr[nr][nc] == '.':
#                             ans = 'impossible'
#                             break
#
#                         elif arr[nr][nc] == '?' or '#':
#                             for t in range(4):
#                                 if 0 <= nr + dr[t] < N and 0 <= nc + dc[t] < M:
#                                     if arr[nr + dr[t]][nc + dc[t]] == '.' or '?':
#                                         pass
#                                     else:
#                                         ans = 'impossible'
#                                         break
#
#
#             if arr[r][c] == '?':    # 시작점이 ? 일 때
#                 for k in range(4):
#                     nr, nc = r + dr[k], c + dc[k]
#                     if 0 <= nr < N and 0 <= nc < M:
#                         if arr[nr][nc] == '.' or '?':
#                             pass
#
#                         elif arr[nr][nc] == '#' or '?':
#                             pass
#
#                         else:
#                             break
#
#             if arr[i][j] == '#':   # 내가 찾은게 # 일 때
#                 for k in range(4):
#                     nr, nc = i + dr[k], j + dc[k]
#                     if 0 <= nr < N and 0 <= nc < M:
#                         if arr[nr][nc] == '#':
#                             ans = 'impossible'
#                             break
#                         else:
#                             pass
#
#             elif arr[i][j] == '.':   # 내가 찾은게 . 일 때
#                 for k in range(4):
#                     nr, nc = i + dr[k], j + dc[k]
#                     if 0 <= nr < N and 0 <= nc < M:
#                         if arr[nr][nc] == '.':
#                             ans = 'impossible'
#                             break
#                         else:
#                             pass
#
#             elif arr[r][c] == '?':  # 내가 찾은 점이 ? 일 때
#                 for k in range(4):
#                     nr, nc = r + dr[k], c + dc[k]
#                     if 0 <= nr < N and 0 <= nc < M:
#                         if arr[nr][nc] == '.' or '?':
#                             pass
#
#                         elif arr[nr][nc] == '#' or '?':
#                             pass
#
#                         else:
#                             break
#
#     print(f'#{tc} {ans}')