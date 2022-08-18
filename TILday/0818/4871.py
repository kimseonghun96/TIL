T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())    # Vertex, Edge 갯수
    adj_matrix = [[0]*(V+1) for _ in range(V+1)] #0은 무시하려고

       #방문 기록 저장
    for i in range(E):
        start, end = map(int, input().split())
        adj_matrix[start][end] = 1  # 노드와 간선 정보 adj_matrix에 저장

    S, G = map(int, input().split())

    stack = [S]
    visited = []

    while stack:  # 스택이 빌때까지
        current = stack.pop ()  # 우선 스택에서 현재 위치 하나 뽑고
        visited.append(current)  # 방문 체크

        for destination in range(V + 1):  # current 입장에서 어디로 갈 수 있는지 모조리 체크
            if adj_matrix[current][destination]:
                stack.append(destination)
        if G in visited:
            print(f'#{tc} 1')
            break

    if G not in visited:
        print(f'#{tc} 0')
