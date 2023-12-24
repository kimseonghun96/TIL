# 1. BFS로 인접한 1을 0으로 바꿔줌.
# 2. 행렬을 만들어 matrix[x][y] = 1인 경우 BFS로 실행. 한 번 실행될 때마다 cnt += 1
# 3. BFS 함수가 인접한 모든 1을 0으로 바꾸므로 연결된 하나의 블럭 개수를 구할 수 있음
#
# 문제 이해를 못했다. 배추흰지렁이는 계속해서 인접한 1로 이동할 수 있는데, 나는 상하좌우 하나 가면 끝나는 줄 알았다. 그래서 출력 5를 이해하지 못했었다...ㅎㅎ...
#
# 문제는 가로길이 M, 세로길이 N으로 줘서 단순하게 M을 열로, N을 행으로 생각했다.
# 이렇게 되면, 기존에 내가 주로 쓰던 N(행)과 M(열)의 생각의 방식을 거꾸로 해야하므로 은근 헷갈렸다. 그러므로 입력받을 때 본인이 주로 쓰던 방식으로 행렬을 입력받는게 좋다.
# N, M의 순서로 입력받았으면 편했을 것이다.
#
# 테두리 범위 (블럭밖으로 나가면 안돼서 지정해주는 범위) 잘 신경써야한다.
#

T = int(input()) #테스트케이스의 개수

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(x,y):
    queue = [(x,y)]
    matrix[x][y] = 0 # 방문처리

    while queue:
        x,y = queue.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue

            if matrix[nx][ny] == 1 :
                queue.append((nx,ny))
                matrix[nx][ny] = 0

# 행렬만들기
for i in range(T):
    M, N, K = map(int,input().split())
    matrix = [[0]*(N) for _ in range(M)]
    cnt = 0

    for j in range(K):
        x,y = map(int, input().split())
        matrix[x][y] = 1

    for a in range(M):
        for b in range(N):
            if matrix[a][b] == 1:
                BFS(a,b)
                cnt += 1

    print(cnt)