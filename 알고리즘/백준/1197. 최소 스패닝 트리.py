# 노드 간선이 너무 어렵다

def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    a = find_set(x)
    b = find_set(y)
    if rank[a] > rank[b]:
        parent[b] = a
    elif rank[a] < rank[b]:
        parent[a] = b
    else:
        parent[b] = a
        rank[a] += 1


v, e = map(int, input().split())  # 노드, 간선
edges = [list(map(int, input().split())) for _ in range(e)]
edges.sort(key=lambda x: x[2])

parent = list(range(v + 1))
rank = [0] * (v + 1)

answer = 0
for a, b, w in edges:
    if find_set(a) != find_set(b):
        union(a, b)
        answer += w

print(answer)


# 노드 간선에 대한 문제
# 트리에 대해서 잘 알아 보자 