
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    # print(arr)

    result = 0          #결과의 초기 값
    start = (0, 0)
    # 시작점을 찾고 싶어요
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                start = (i, j)

    flag = True
    stack = [start, ]
    visited = set()
    while stack and flag:
        pick = stack.pop()  # pick[0, 1]
        x = pick[0]
        y = pick[1]
        for direction in range(4):   # direction = [ 0, 1, 2, 3 ]
            px = x + di[direction]
            py = y + dj[direction]
            if 0 <= px < N and 0 <= py < N and (px, py) not in visited:
                if arr[px][py] == '3':
                    result = 1
                    flag = False
                    break
                elif arr[px][py] == '0':
                    stack.append((px, py))
                    visited.add((px, py))


    print(f'#{tc} {result}')



