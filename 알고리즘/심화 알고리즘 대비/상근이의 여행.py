# 최소 신장 트리의 성질을 이용한다. 간선의 개수는 정점의 개수-1 이다.
# 즉, 모든 국가가 연결되어 있기 때문에 비행기 종류의 최소 개수는 국가 수 - 1이다.

import sys

input = sys.stdin.readline

# 모든 국가가 연결되 어 있으면 비행기 종류의 최소 개수는 국가 수 -1이다.
# T = int(input())
#
# for tc in range(T):
#     n, m = map(int, input().split())
#     for i in range(m):
#         a, b = map(int, input().split())
#
#     print(n-1)
#

def dfs(node, cnt):
    visit[node] = 1  # 현재 노드를 방문했음을 표시
    for i in Tree[node]:  # 현재 노드와 연결된 모든 이웃 노드에 대해서
        if visit[i] == 0:  # 이웃 노드를 방문하지 않았다면
            cnt = dfs(i, cnt + 1)  # 이웃 노드로 이동하고 cnt(길이)를 1 증가시킴
    return cnt  # 최종적으로 현재 노드를 루트로 하는 서브트리의 길이를 반환

T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    Tree = [[] for _ in range(n+1)]  # 노드와 이웃 관계를 저장하는 그래프를 초기화
    for _ in range(m):
        a, b = map(int, input().split())
        Tree[a].append(b)  # 노드 'a'와 'b'를 서로 연결
        Tree[b].append(a)  # 양방향 그래프를 만들기 위해 'b'도 'a'와 연결

    visit = [0] * (n+1)  # 노드의 방문 여부를 나타내는 리스트를 초기화
    visit[1] = 0  # 첫 번째 노드를 시작 노드로 설정
    result = dfs(1, 0)  # DFS 함수를 시작 노드(1)에서 호출하고, 초기 길이를 0으로 설정
    print(result)  # 결과 출력