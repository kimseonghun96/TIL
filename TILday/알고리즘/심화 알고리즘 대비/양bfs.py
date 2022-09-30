'''
9 12
.###.#####..
#.oo#...#v#.
#..o#.#.#.#.
#..##o#...#.
#.#v#o###.#.
#..#v#....#.
#...v#v####.
.####.#vv.o#
.......####.
'''

# 울타리 안에 들어가게 되면 양과 늑대의 수를 세아릴 bfs 만듬
# 조건에 맞게 양과 늑대 마리수 출력


def bfs(r, c):
    global w, s
    visit[r][c] = 1         # 방문 한 곳은 1
    queue.append((r, c))    # queue 에 담음

    while queue:
        pick = queue.pop(0)         # 앞의 것 부터 r, c에 저장할 거기 때문에 pop(0)
        r, c = pick

        if arr[r][c] == 'v':                # 늑대 찾으면 +1
            w += 1

        elif arr[r][c] == 'o':              # 양 찾으면 +1
            s += 1

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            # 범위 설정, 벽이 아니고, 방문을 안했다면
            if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] != '#' and not visit[nr][nc]:
                queue.append([nr, nc])          # queue 에 추가
                visit[nr][nc] = 1               # 방문 기록


dr = [-1, 0, 1, 0]      # 상 하 좌 우
dc = [0, 1, 0, -1]

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
# print(arr)

queue = []
visit = [[0] * C for _ in range(R)]
# print(visit)

wolf = 0
sheep = 0

for k in range(R):
    for t in range(C):
        if arr[k][t] != '#' and visit[k][t] == 0:   # 벽이 아니고 방문한 곳이 아니면
            w = 0                   # 돌 때마다 초기화
            s = 0
            bfs(k, t)               # bfs 작동

            if w >= s:              # 수 비교
                s = 0
            else:
                w = 0

            wolf += w
            sheep += s

print(sheep, wolf)















