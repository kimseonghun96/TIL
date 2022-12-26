'''
4
5
....o
...o.
..o..
.o...
o....
5
...o.
ooooo
...o.
...o.
.....
5
.o.oo
oo.oo
.oo..
.o...
.o...
5
.o.o.
o.o.o
.o.o.
o.o.o
.o.o.
'''
dr = [-1, 1, 0, 0, -1, 1, 1, -1]
dc = [0, 0, -1, 1, -1, -1, 1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    ans = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'o':
                for k in range(8):
                    cnt = 1
                    for t in range(1, 5):
                        nr, nc = r + dr[k] * t, c + dc[k] * t
                        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == '.':
                            break
                        elif 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 'o':
                            cnt += 1

                    if cnt == 5:
                        ans = cnt

    if ans == 5:
        print('yes')
    else:
        print('no')




