N,M,V = map(int,input().split()) # 노드의 개수, 간선의 개수, 탐색 시작 노드

graph = [[0]*(N+1) for _ in range(N+1)]
for i in range (M):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1  # 접점 연결

#방문 리스트 행렬
visited1 = [0]*(N+1)
visited2 = visited1.copy()

#dfs 함수 만들기
def dfs(V):
    visited1[V] = 1 #시작점 방문처리
    print(V, end=' ')
    for i in range(1, N+1):
        if graph[V][i] == 1 and visited1[i] == 0:  # 연결 확인, 스택에 들어간 적이 있는지 확인
            dfs(i) # 다음 재귀


#bfs 함수 만들기
def bfs(V):
    queue = [V]     #방문 노드 저장
    visited2[V] = 1 #방문처리
    while queue:    #queue에 값이 없을때까지
        print('queue:', queue)
        V = queue.pop(0) #방문 노드 제거
        print(V, end = ' ')
        for i in range(1, N+1):
            if(graph[V][i] == 1 and visited2[i] == 0):
                queue.append(i)   # 연결된 노드 큐에 추가
                visited2[i] = 1 # 방문처리


dfs(V)
print()
bfs(V)