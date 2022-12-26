import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0]
dy = [0, 0, -1]

for tc in range(10):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    #첫 시작점은 도착(마지막 줄) 지점2
    x = ladder[99].index(2)
    y = 99         # 밑에서부터 올라갈꺼임
    k = 0          # ?

    # y가 0인덱스까지 도달할때까지 반복한다.
    while y > 0:
        nx = x + dx[k]  #이동하고자하는 곳으로 이동
        ny = y + dy[k]

        # 전체 사다리에서 나가지 않고,  1 일 때 조건문 실행
        if 0 <= nx < 100 and 0 <= ny < 100 and ladder[ny][nx]:
            ladder[ny][nx] = 0  # 지나온 자리를 0으로 바꿔준다. (중복 탐색 방지를 위해)
            x = nx              # x를 nx로 업뎃
            y = ny              # y를 ny로 업뎃
            k = 0               # k를 맨 처음으로 초기화. (이동한 곳에서 다시 탐색해야 하므로)

        # 이동하고자 하는 곳이 전체 사다리 범위에서 벗어나거나, 사다리로 이어진 부분이 아니라면(0일경우)
        else:
            # 방향을 바꿔준다.
            k = (k+1) % 3

    # y가 0이라면 시작지점에 도달한 것이므로 x좌표를 출력한다.
    print(f'#{N} {x}')

dx = [-1, 0, 0]
dy = [0, 1, -1]

t = 10
for tc in range(t):
    n = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    # print(n, arr)
    x, y = 0, 0
    d = 0
    for i in range(100):
        for j in range(102):
            if arr[i][j] == 2:
                x = i
                y = j

        while True:
            if x == 0:
                break

            if arr[x][y - 1] == 1:  # 왼쪽으로 가기
                d = 2
                while True:
                    x += dx[d]
                    y += dy[d]
                    if arr[x][y - 1] == 0:
                        break
            elif arr[x][y + 1] == 1:  # 오른쪽으로 가기
                d = 1
                while True:
                    x += dx[d]
                    y += dy[d]
                    if arr[x][y + 1] == 0:
                        break

            d = 0
            x += dx[0]
            y += dy[0]

    print(f'#{tc + 1} {y - 1}')
