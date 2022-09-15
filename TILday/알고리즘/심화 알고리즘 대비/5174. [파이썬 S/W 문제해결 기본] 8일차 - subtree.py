T = int(input())
for tc in range(1, T+1):
    def find_root(V):
        for i in range(1, V+1):
            if par[i] == 0:
                return i


    def postorder(n):  # 후위순회
        if n:
            postorder(left[n])
            postorder(right[n])
            print(n)  # visit(n)


    E, N = input().split()
    E = int(E)
    N = int(N)
    V = E + 1  # 노드 개수
    N_ch = list(map(int, input().split()))
    # 오른쪽, 왼쪽
    left = [0]*(V+1)
    right = [0]*(V+1)
    # 부모
    par = [0]*(V+1)
    for i in range(E):
        p, c = N_ch[i*2], N_ch[i*2+1]

        if left[p] == 0:     #아직 자식이 없으면
            left[p] = c      # left 로 저장
        else:
            right[p] = c
        par[c] = p

    root = find_root(V)
    # print(root)
    if p == N:
        print(f'#{tc}', left)