di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

T = 10
for tc in range(1, T+1):
    testcase = int(input())
    arr = [list(input()) for _ in range(16)]
    # print(arr)

    result = 0          #결과의 초기 값
    start = (0, 0)
    # 시작점을 찾고 싶어요
    for i in range(16):
        for j in range(16):
            if arr[i][j] == '2':
                start = (i, j)


            # 시작점에서 시작

            # '밟은 곳에서 사방탐색하면서 0을 찾아
            # 스택에 담음
            # 움직일 건데 스택에서 하나를 빼서 그 좌표로 이동
            # 현재위치를 기록함'
            # 3을 찾았을 때 result =1
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
            if 0 <= px < 16 and 0 <= py < 16 and (px, py) not in visited:
                if arr[px][py] == '3':
                    result = 1
                    flag = False
                    break
                elif arr[px][py] == '0':
                    stack.append((px, py))
                    visited.add((px, py))

    print(f'#{testcase} {result}')
