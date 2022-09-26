'''
3
5 1
2 1 2 5 1 6 5 3 6 4
5 1
2 6 6 4 6 5 4 1 5 3
10 5
7 6 7 4 6 9 4 11 9 5 11 8 5 3 5 2 8 1 8 10
'''



# def postorder(n):
#     global answer
#     # 순회할 때마다 + 1
#     answer += 1
#     postorder(left[n])
#     postorder(right[n])


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))
    V = E + 1
    left = [0]*(V+1)
    right = [0]*(V+1)
    for i in range(E):
        parent, child = edges[2*i], edges[2*i+1]
        if left[parent]:
            right[parent] = child
        else:
            left[parent] = child

    stack = [N]
    visit = []
    while stack:
        current = stack.pop()
        visit.append(current)

        if left[current]:
            stack.append(left[current])
        if right[current]:
            stack.append(right[current])

    # print(visit)
    print(f'#{tc} {len(visit)}')



def cnt_node(n):
    global cnt
    if n:
        cnt += 1
        cnt_node(left[n])
        cnt_node(right[n])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))
    V = E+1
    left = [0]*(V+1)
    right = [0]*(V+1)
    for i in range(E):
        parent = edges[2*i]
        child = edges[2*i+1]

        if not left[parent]:
            left[parent] = child
        else:
            right[parent] = child

    cnt = 0
    cnt_node(N)

    print(f'#{tc} {cnt}')