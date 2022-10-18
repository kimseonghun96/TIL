'''
1
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3
'''
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for r in range(N-M+1):
        for c in range(N-M+1):
            temp = 0
            for i in range(r, r+M):
                for j in range(c, c+M):
                    if 0 <= i < N and 0 <= j < N:
                        temp += arr[i][j]
                        # print(temp)
            if ans < temp:
                ans = temp

    print(f'#{tc} {ans}')
