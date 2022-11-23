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

# 각 해당줄의 색의 개수가 가장 큰 것을뽑아
# 전체 수에서 빼면
# 그 값이 가장 적게 변경되는 값
T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    w_list = []
    b_list = []
    r_list = []

    for r in range(1, N-1):                             # 세로 3 분할
        for c in range(r+1,N):
            w_list.append(arr[0:r][:])               # 한줄씩 담는거(전에 담겼던게 중복해서 담김)
            b_list.append(arr[r:c][:])
            r_list.append(arr[c:N][:])
    # print(w_list)
    #         print(arr[0:r][:])
    # print(len(w_list))
    # print(w_list)
    case = 0                        # 총 케이스가 중복해서 대해 지므로 1 C case
    for i in range(1, N-1):
        case += i
    # print(case)


    ans = 0
    for i in range(case):                # 총 케이스가 중복해서 대해 지므로 1 C case
        w_cnt = 0
        b_cnt = 0
        r_cnt = 0
        for j in range(len(w_list[i])):             # 줄의 해당색을 더해줌
            w_cnt += w_list[i][j].count('W')

        for j in range(len(b_list[i])):
            b_cnt += b_list[i][j].count('B')

        for j in range(len(r_list[i])):
            r_cnt += r_list[i][j].count('R')

        if  ans < w_cnt + b_cnt + r_cnt:        # 가장 큰 값 추출
            ans = w_cnt + b_cnt + r_cnt

    ans = N*M - ans

    print(f'#{tc} {ans}')



