'''
6 6
...#..
.##v#.
#v.#.#
#.o#.#
.###.#
...###
'''
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
w, s = 0, 0   # 늑대와 양 수
# 시작점 정의
start = (0,0)
stack = [start, ]
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

    if s > w:
        w = 0
    else:
        s = 0

    print(w, s)
