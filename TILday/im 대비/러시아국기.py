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
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    w_list = []
    b_list = []
    r_list = []

    for i in range(1, N - 1):               # 3등분 하는 거
        for j in range(i + 1, N):
            w_list.append(arr[0:i][:])
            b_list.append(arr[i:j][:])
            r_list.append(arr[j:N][:])
    ru_max = 0                                # 바꾼 거

    for i in range(len(w_list)):
        w_count = 0
        b_count = 0
        r_count = 0
        for j in range(len(w_list[i])):
            w_count += w_list[i][j].count('W')

        for j in range(len(b_list[i])):
            b_count += b_list[i][j].count('B')

        for j in range(len(r_list[i])):
            r_count += r_list[i][j].count('R')

        if ru_max < w_count + b_count + r_count:
            ru_max = w_count + b_count + r_count

    ans = N * M - ru_max

    print(f'#{tc} {ans}')