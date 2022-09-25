import sys
sys.stdin = open('input.txt')

dr= [-1, 0, 0]
dc= [0, -1, 1]

for tc in range(10):
    testcase = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    #첫 시작점은 도착(마지막 줄) 지점2
    # r = int(ladder[99].index(2))
    # c = 99
    start = (0, 0)
    for r in range(100):
        for c in range(100):
            if ladder[r][c] == 2:
                start = (r, c)

    stack = [start, ]
    visit = set()
    end = []    # 마지막 좌표 찍을 꺼임
    while stack: # 스택 빌 때까지 돈다.
        current = stack.pop()
        r = current[0]
        c = current[1]
        # print(c)
        for i in range(3):
            if ladder[r][c] == 1:
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < 100 and 0 <= nc < 100 and (nr, nc) not in visit:
                    if ladder[nr][nc] == 1:
                        stack.append(ladder[nr][nc])
                        visit.add(ladder[nr][nc])
                        ladder[nr][nc] = 0

        if c == 0 and ladder[r][c] == 1:

# dx = [-1, 0, 0]
# dy = [0, 1, -1]
#
# t = 10
# for tc in range(t):
#     n = int(input())
#     arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
#     # print(n, arr)
#     x, y = 0, 0
#     d = 0
#     for i in range(100):
#         for j in range(102):
#             if arr[i][j] == 2:
#                 x = i
#                 y = j
#
#         while True:
#             if x == 0:
#                 break
#
#             if arr[x][y - 1] == 1:  # 왼쪽으로 가기
#                 d = 2
#                 while True:
#                     x += dx[d]
#                     y += dy[d]
#                     if arr[x][y - 1] == 0:
#                         break
#             elif arr[x][y + 1] == 1:  # 오른쪽으로 가기
#                 d = 1
#                 while True:
#                     x += dx[d]
#                     y += dy[d]
#                     if arr[x][y + 1] == 0:
#                         break
#
#             d = 0
#             x += dx[0]
#             y += dy[0]
#
#     print(f'#{tc + 1} {y - 1}')