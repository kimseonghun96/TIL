'''
8주차에 교제 있음
이진트리는 자식이 많아야 2개다. 적으면 0
자식이 없을 경우 -> 리프 노드/ 이진트리일 경우  오른쪽, 왼쪽 둘 다 0
int는 뒤의 소수점을 버린다. -> 버림연산

트리는 특성상 순회는 재귀함수로 해야함
def preorder(T):    # 전위순회
    if T:
        visit(V)    #visit(n)
        preorder(T.left)
        preorder(T.right)

 -> 부모노드 방문 후, 자식노드를 좌,우 순서로 방문한다.(도착하자 말자 찍음)

def inorder(n):    # 중앙순회
    if n:
        inorder(ch1[n])
        print(n)  # visit(n)
        inorder(ch2[n])

-> 왼쪽 자식노드, 부모노드, 오른쪽 자식노드 순으로 방문.(끝까지 왼쪽갔다가 왼쪽에서 돌아나올 때 찍음)

def postorder(n):    # 후위순회
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n)  # visit(n)

->자식노드를 좌우 순서로 방문한 후, 부모노드로 방문한다. (오른쪽에서 돌아 나올 때 찍힌다.)
'''