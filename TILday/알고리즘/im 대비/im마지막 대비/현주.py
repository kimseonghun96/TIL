'''
1
5 2
1 3
2 4
'''
T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    arr = [0] * (N+1)
    num = 1
    for i in range(Q):
        L, R = map(int, input().split())
        for j in range(L, R+1):
            arr[j] = num
        num += 1
    ans = []
    for i in range(1, N+1):
        ans.append(arr[i])

    print(f'#{tc}', *ans)
