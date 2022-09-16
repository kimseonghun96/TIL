'''
3
5 3 2
4 1
5 2
3 3
10 5 2
8 42
9 468
10 335
6 501
7 170
17 9 4
16 479
17 359
9 963
10 465
11 706
12 146
13 282
14 828
15 962

'''
def post_order(leaf):                    # 후위순회
    if leaf <= N and not tree[leaf]:
        post_order(leaf*2)
        post_order(leaf*2+1)
        tree[leaf] = tree[leaf*2]+tree[leaf*2+1]  # 왼쪽 오른쪽 더하면서 올라감
T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())  #노드의 개수, 리프노드의 개수, 출력할 노드 번호
    tree = [0] * (N + 2)   # 마지막 노드의 오른쪽이 없는 경우 error 발생

    for _ in range(M):   # 리프 노드 번호와 자연수 저장
        leaf, number = map(int, input().split())
        tree[leaf] = number

    post_order(1)

    print(f'#{tc} {tree[L]}')