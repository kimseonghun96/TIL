# 오목 판정 im에 비슷한 문제가 제출됨
# 델타를 이용 기준위치를 잡아서 상하좌우에 해당하는 좌표 생성

N, K = 10, 4         # N:총 길이 K: 몇칸 가는지
arr = [[0]*N for _ in range(N)]

dr = [-1, 1, 0, 0]          # 상, 하
dc = [0, 0, -1, 1]          # 좌, 우

# dr = [-1, -1, 1, 1]          # 대각선
# dc = [-1, 1, 1, -1]

r = c = 3             # N = 7일 경우 중앙, 기준
arr[r][c] = '*'

# arr[r-1][c+0] = 1         # 상
# arr[r+1][c+0] = 1         # 하
# arr[r+0][c-1] = 1         # 좌
# arr[r+0][c+1] = 1         # 우
'''
상하좌우 쭉 가는거 풀었는 법

for i in range(r -1, -1, -1): # 상  위로 쭉가는거
    arr[i][c] = 1

for i in range(r + 1, N):  # 하 아래로 가는 것
    arr[i][c] = 2

for i in range(c -1, -1, -1):  # 좌
    arr[r][i] = 3

for i in range(c +1, N):  # 우
    arr[r][i] = 4
'''

for i in range(4):
    for j in range(1, K+1):      # 중간점은 따로 찍고, 반복을 최대치로 해주고 나중에 끊을 거임
    # (r, c) => 4방향 좌표를 생성
        nr = r + dr[i]*j
        nc = c + dc[i]*j
        # if 0 <= nr < N and 0 <= nc < N:   # 범위 안에 들어오면, 밖으로 나가는 경우, 인덱스 에러를 막기 위해 경계 설정, 벗 멈추는게 없어서 계속 돔
        if nr < 0 or nr >= N or nc < 0 or nc >= N: # 경계 체크 중요
            break
        arr[nr][nc] = i + 1


for line in arr:
    print(*line)

