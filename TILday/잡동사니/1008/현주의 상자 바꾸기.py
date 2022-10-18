'''
1
5 2
1 3
2 4
'''
T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    box = [0] * (N + 1)
    ans = []
    for i in range(1, Q+1):
        start, end = map(int, input().split())
        for j in range(start, end+1):
            box[j] = i
    # print(box)
    for i in range(1, len(box)):
        ans.append(box[i])

    print(f'#{tc}', *ans)
