'''
1
1111111111111111
1210000000100011
1010101110101111
1000100010100011
1111111010101011
1000000010101011
1011111110111011
1010000010001011
1010101111101011
1010100010001011
1010111010111011
1010001000100011
1011101111101011
1000100000001311
1111111111111111
1111111111111111
'''
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


for tc in range(10):
    testcase = int(input())
    arr = [list(input()) for _ in range(16)]
    ans = 0

    # print(arr)
    start = (0, 0)
    for r in range(16):
        for c in range(16):
            if arr[r][c] == '2':
                start = (r, c)

    # print(start)
    stack = [start, ]
    visited = set()
    while stack:
        pick = stack.pop()
        x = pick[0]
        y = pick[1]
        for k in range(4):
            nr, nc = x + dr[k], y + dc[k]
            if 0 <= nr < 16 and 0<= nc < 16 and (nr, nc) not in visited:
                if arr[nr][nc] == '3':
                    ans = 1
                    break

                elif arr[nr][nc] == '0':
                    stack.append((nr, nc))
                    visited.add((nr, nc))

    print(f'#{testcase} {ans}')
