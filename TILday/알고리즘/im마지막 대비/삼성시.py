'''
1
2
1 3
2 5
5
1
2
3
4
5
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bus_idx = [0] * 5001
    ans = []
    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B+1):
            bus_idx[j] += 1

    P = int(input())
    for k in range(1, P+1):
        ans.append(bus_idx[int(input())])

    print(f'#{tc}', *ans)





