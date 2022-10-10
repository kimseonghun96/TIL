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

    sam_bus = [0] * 5001
    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B+1):
            sam_bus[j] += 1

    # print(sam_bus)
    P = int(input())
    ans = []
    for i in range(P):
        num = int(input())
        ans.append(sam_bus[num])

    print(f'#{tc}', *ans)

