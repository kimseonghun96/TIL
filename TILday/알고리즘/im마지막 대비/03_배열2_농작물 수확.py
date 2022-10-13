'''
1
5
2 3 2 2 1
3 1 1 1 3
3 2 3 1 3
1 1 3 2 1
2 2 2 1 1
5
3 3 2 1 1
2 1 1 3 1
3 1 3 3 2
3 1 2 2 3
2 3 1 2 2
5
1 3 2 1 3
3 1 3 2 1
3 3 1 1 2
1 3 2 2 1
1 2 3 3 2
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 999999
    for r in range(1, N):
        for c in range(1, N):
            temp1 = 0
            temp2 = 0
            temp3 = 0
            temp = []
            for i in range(0, r):                 # temp1
                for j in range(0, c):
                    temp.append(arr[i][j])

            for i in range(r, N):                 # temp2
                for j in range(0, c):
                    temp.append(arr[i][j])

            for i in range(0, N):                 # temp3
                for j in range(c, N):
                    temp.append(arr[i][j])
            print(temp)
            if ans > max(temp) - min (temp):
                ans = max(temp) - min (temp)

    print(f'#{tc} {ans}')








































