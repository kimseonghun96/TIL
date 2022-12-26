'''
2
4 5
WRWRW
BWRWB
WRWRW
RWBWR
6 14
WWWWWWWWWWWWWW
WWRRWWBBBBBBWW
WRRRWWWBWWWWRB
WWBWBWWWBWRRRR
WBWBBWWWBBWRRW
WWWWWWWWWWWWWW
'''
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    w_list = []
    b_list = []
    r_list = []
    for i in range(1, N-1):
        for j in range(i+1, N):
            w_list.append(arr[0:i][:])
            b_list.append(arr[i:j][:])
            r_list.append(arr[j:N][:])

    case = 0
    for i in range(1, N-1):
        case += i

    ans = 0
    for i in range(case):
        w_cnt = 0
        b_cnt = 0
        r_cnt = 0
        all_sum = 0
        for j in range(len(w_list[i])):
            w_cnt += w_list[i][j].count('W')

        for j in range(len(b_list[i])):
            b_cnt += b_list[i][j].count('B')

        for j in range(len(r_list[i])):
            r_cnt += r_list[i][j].count('R')
        # print(w_cnt)
        if ans < w_cnt + b_cnt + r_cnt:
            ans = w_cnt + b_cnt + r_cnt

    ans = N*M - ans

    print(ans)

