# 완전 이진트리 - 중위 순회하는 문제!
# 완전 이진트리의 노드 개수는 2 * 깊이(k) -1 이다. 이 문제에선 len(nodes)와 같다.
# 완전 이진트리는 각 층마다 인덱스가 두배로 뛰기 때문에 1을 시작으로 한층을 출력하고,
# 인덱스를 두배로 증가시켜 다음층을 출력하면된다.


# def inorder(node):
#     global idx
#
#     if node < n:
#         inorder(node*2)
#         tree[node] = nodes[idx]   #
#         idx += 1
#         inorder(node*2+1)
#
#
# N = int(input())
# nodes = list(map(int, input().split()))
# n = 2**N   # -1을 뺀 이유, 노드의 개수에 +1 해준 이유는 0번 인덱스는 사용 x
# tree = [0] * 2**N
# idx = 0
#
# # def inorder(node):
# #     global idx
# #
# #     if node < n:
# #         inorder(node*2)
# #         tree[node] = nodes[idx]
# #         idx += 1
# #         inorder(node*2+1)
#
# inorder(1)
# idx = 1  # 1번에서 출력
# while idx < n:
#     for i in range(idx, idx*2):
#         print(tree[i], end = ' ')
#     print()
#     idx *= 2 # 두배로 만든 후 반복


def inorder(node):
    global idx
    if node < len(nodes) +1 :  # idx 0은 사용하지 않을 것
        inorder(node * 2)
        tree[node] = nodes[idx]
        idx += 1
        inorder(node * 2 +1)


K = int(input())
nodes = list(map(int, input().split()))
# 노드의 2 ** 깊이 -1 ->  2**K +1 == len(nodes)
tree = [0] * (len(nodes) + 1)  #첫번째 인덱스 사용하지 않음
idx = 0
inorder(1)
idx = 1
while idx < len(nodes)+1:
    for i in range(idx, idx*2):
        print(tree[i], end = ' ')
    print()
    idx *=2