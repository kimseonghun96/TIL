'''
3
6
8
15
'''


def inorder(n):
    if n <= N:
        global number
        left, right = n*2, n*2+1
        inorder(left)
        tree_idx[n] = number
        number += 1
        inorder(right)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree_idx = [0] * (N+1)
    number = 1
    inorder(1)

    print(f'#{tc} {tree_idx[1]} {tree_idx[N//2]}')
