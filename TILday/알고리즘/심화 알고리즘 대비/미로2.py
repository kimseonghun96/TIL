dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = 10
for tc in range(1, T+1):
    testcase = int(input())
    arr = [list(input()) for _ in range(100)]

    ans = 0
    start = (0, 0)
    for x in range(100):
        for y in range(100):
            if arr[x][y] == '2':
                start = (x, y)

    flag = True
    stack = [start, ]
    visited = set()
    while stack and flag:
        current = stack.pop()
        nx 0= current[0]
        ny = current[1]
        # print(stack)
        for i in range(4):
            px = nx + dx[i]
            py = ny + dy[i]
            if 0 <= px < 100 and 0 <= py < 100 and (px, py) not in visited:
                if arr[px][py] == '3':
                    result = 1
                    flag = False
                    break

                elif arr[px][py] == '0':
                    stack.append((px, py))
                    visited.add((px, py))

    print(f'#{testcase} {ans}')

