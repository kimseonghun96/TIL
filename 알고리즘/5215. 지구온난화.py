import sys
import copy

R, C = map(int, sys.stdin.readline().split())

arr = [list(input()) for _ in range(R)]
result = copy.deepcopy(arr)   # 원본 객체와 복사본 객체는 완전히 독립적

dy = [-1, 0, 1, 0] # 상   하
dx = [0, -1, 0, 1] #    좌   우

for y in range(R):
    for x in range(C):
        count = 0
        if arr[y][x] == '.':
            continue

        elif arr[y][x] == 'X':
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < R and 0 <= nx < C:
                    if arr[ny][nx] == '.':
                        count += 1
                else:  # 범위를 넘어가는 경우도 바다
                    count += 1
            if count >= 3:
                result[y][x] = '.'

start_y, end_y = 0, 0  # 섬의 시작 행과 종료 행
for i in range(R):
    if 'X' in result[i]:
        start_y = i
        break
for i in range(R - 1, -1, -1): # 역방향으로 검색
    if 'X' in result[i]:
        end_y = i
        break

# print(start_y, end_y) [1, 2]

temp = []
for j in range(C):
    for i in range(start_y, end_y + 1):
        if 'X' == result[i][j]:
            temp.append(j)
            break

# print(temp)  [1, 2, 3, 7]
# temp[0]은 해당 행에서 섬이 시작하는 열의 인덱스를,
# temp[-1]은 해당 행에서 섬이 끝나는 열의 인덱스

for y in range(start_y, end_y + 1):
    print("".join(result[y][temp[0]:temp[-1] + 1]))