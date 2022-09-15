'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
'''
def find_root(V):
    for i in range(1, V + 1):
        if par[i] == 0:  # 부모가 없으면 root
            return  i

def preorder(n):    # 전위순회
    if n:
        print(n, end=' ')    #visit(n)
        preorder(ch1[n])
        preorder(ch2[n])

def inorder(n):    # 중앙순회
    if n:
        inorder(ch1[n])
        print(n)  # visit(n)
        inorder(ch2[n])

def postorder(n):    # 후위순회
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n)  # visit(n)

V = int(input())    # 정점 개수, 마지막 정점번호
arr = list(map(int, input().split()))
E = V - 1

# 부모를 인덱스로 자식 번호 저장
ch1 = [0]*(V+1)
ch2 = [0]*(V+1)
# 자식을 인덱스로 부모 번호 저장
par = [0]*(V+1)
for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
# for j in range(0, E*2, 2):   위와 같은 방법
#     p, c = arr[j], arr[j+1]
    if ch1[p] == 0:     #아직 자식이 없으면
        ch1[p] = c      # 자식 1로 저장
    else:
        ch2[p] = c
    par[c] = p

root = find_root(V)
# print(root)

preorder(root)
# inorder(root)
# postorder(root)
'''




'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
#전위 순회 => print / 왼/ 오

V = int(input())
edges = list(map(int, input().split()))
left = [0]*(V+1)
right = [0]*(V+1)
find_root = [0]*(V+1)
root = None  #일단 루트 모름
for i in range(V-1): # 간선의 개수만큼 돌면서
    parent, child = edges[2*i], edges[2*i+1]
    if not left[parent]: #left[parent]==0:
        left[parent] = child
    else:
        right[parent] = child

    find_root[child] = parent

# print('왼: ', left)
# print('오: ', right)

def preorder(n): # n은 노드 번호
    if n > 0:
        print(n, end = ' ')
        preorder(left[n])
        # print(n, end=' ')
        preorder(right[n])
        # print(n, end=' ')

for j in range(1, V+1):
    if find_root[j] == 0:
        root = j
        break

preorder(root)
print()
print(root)