import sys
sys.stdin = open('input.txt')

V, E = map(int, input().split())  # Vertex, Edge 갯수 7, 8

adj_matrix = [[0]*(V+1) for _ in range(V+1)] # 인접행렬 기본틀 8x8 [0]으로 채워짐

for _ in range(E):     # 돌기만 할때는  _ , 간선 갯수만큼 돌면서 연결 정보를 받음
    start, end = map(int, input().split()) # 시작점과 끝점
    adj_matrix[start][end] = 1          # 양 방향 그래프
    adj_matrix[end][start] = 1

# print(adj_matrix)

stack = [1]   # 시작점 1
visited = []  # 방문한 곳 기록

while stack: # stack 빌 때까지 돌자
    current = stack.pop()  # pop 은 뽑자말자 리턴 값을 줌 현재 위치가 담김
    if current not in visited:      # visited 에 없다면
        visited.append(current)     # 방문기록 체크         stack 에 담긴 1이 pop 되고 visited 에 담김

    for destination in range(V+1): # current 입장에서 어디로 갈 수 있는지 모조리 체크
        if adj_matrix[current][destination] and destination not in visited: # 갈수있고 + 방문 안했으면!
            stack.append(destination)   # 다음 갈 곳으로 stack 에 저장

print(visited)

#    print(stack)   stack 은 반복하면서 방문했기 때문에 하나씩 버려짐





# V, E = map(int, input().split())
#
# adj_matrix = [[0]*(V+1) for _ in range(V+1)]
#
# for _ in range(E):
#     start, end = map(int, input().split())
#     adj_matrix[start][end] = 1
#     adj_matrix[end][start] = 1
#
# stack = [1]
# visited = []
#
# while stack:
#     current = stack.pop()
#     if current not in visited:
#         visited.append(current)
#
#     for destination in range(V+1):
#         if adj_matrix[current][destination] and destination not in visited:
#             stack.append(destination)
#
# print(visited)
