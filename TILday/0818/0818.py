T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())    # Vertex, Edge 갯수
    adj_matrix = [[0]*(V+1) for _ in range(V+1)] #0은 무시하려고

       #방문 기록 저장
    for i in range(E):
        start, end = map(int, input().split())
        adj_matrix[start][end] = 1  # 노드와 간선 정보 VE_matrix에 저장

    S, G = map(int, input().split())

    stack = [S]
    visited = []

    while stack:  # 스택이 빌때까지 돌아라!
        current = stack.pop ()  # 우선 스택에서 현재 위치 하나 뽑고
        if current not in visited:  # 방문하지 않은 곳이라면,
            visited.append(current)  # 방문했다고 체크해줌

        for destination in range(V + 1):  # current 입장에서 어디로 갈 수 있는지 모조리 체크
            if adj_matrix[current][destination]:  # 갈수있고 + 방문 안했으면!
                stack.append(destination)  # 다음 갈 곳으로 Stack에 저장        # 여러가지 길을 타고가도 길이 있으면 1을 출력해야되기 때문에 스택을 사용해야댐
        #출발 노드S와 도착노드 G가 주어지기 때문에 받는 곳을 만들어야됨

    result = 0
    for i in range(len(visited)):
        if visited[i] == adj_matrix[S] and visited[i] == adj_matrix[G]:
            result = 1
        else:
            result = 0      #굳이 적을 필요는 없을 듯?

    print(f'#{tc} {result}')


