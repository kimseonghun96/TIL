T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = list(map(int, input().split()))

    finish = max(tree)

    temp = []
    for i in range(N):
        temp.append(finish - tree[i])

    temp1 = []    # 몫
    temp2 = []    # 나머지

    for i in range(len(temp)):
        temp1.append(sum(temp)//3)
        temp2.append(sum(temp) % 3)

    ans = 0
    for i in range(len(temp1)):
        ans = temp1[i]*2 + temp2[i]

    print(f'#{tc} {ans}')