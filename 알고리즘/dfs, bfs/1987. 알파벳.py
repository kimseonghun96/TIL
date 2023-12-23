# 알고리즘 선택 이유
# 1. 넓게 가는 것이 아닌 깊게 멀리 가야하기 때문에
# 2. 분기별로 최장 길이를 구하여 비교해야 하기 때문에
#
# 예외처리
#
# 갈 수 없는 곳(좌측상단일 경우 좌, 상으로 이동할 수 없음) 처리
# dfs 가 끝나는 지점에서 visited를 False로 알파벳은 가장 최근에 들어간 알파벳을 제거해주어야 함 --> 이걸 하지 않으면 이미 방문한 것으로 간주하여 최적의 루트를 찾을 수 없음
# dfs 종료조건으로는 더 이상 나아갈 길이 없을 경우 종료
# 재귀 함수에서 max 값을 비교해야 하는데 이 부분 어떻게 하는 지 모름 --> 하단 코드 참고(global dist 식으로 변수 선언하면 재귀 함수 내에서 비교 가능)
# 해결 방법
# 1. 알파벳만 visited 배열로 체크해 주면 됨 --> 굳이 이동하는 곳(즉 버택스는 체크 불필요)
# 2. 최장 거리를 비교해야 하기 때문에 방문을 완료했을 때 최적인지 아닌지 모르므로 백트래킹하여 최적의 거리 검색
#

import sys

r, c = list(map(int, sys.stdin.readline().split()))
graph = [[0 for x in range(c)] for x in range(r)]
for i in range(r):
    temp = sys.stdin.readline()
    for k in range(c):
        graph[i][k] = temp[k]

visited = [False for x in range(26)]

def dfs(x, y, visited, depth):
    global dist
    dist = max(dist, depth)
    n = graph[x][y]
    visited[ord(n)-65] = True
    adj_list = [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]
    check = 0
    for point in adj_list:
        px = point[0]
        py = point[1]
        if px >= 0 and px < r and py >=0 and py < c:
            n = graph[px][py]
            if visited[ord(n)-65] == False:
                check += 1
                dfs(px, py, visited, depth + 1)
                visited[ord(n)-65]=False


global dist
dist = 0
dfs(0, 0, visited, 1)
print(dist)