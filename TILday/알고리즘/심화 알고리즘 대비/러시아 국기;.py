import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    # print(arr)
    w_list = []
    b_list = []
    r_list = []

    for i in range(1, N-1):
        for j in range(i+1, N):
            w_list.append(arr[0:i][:])
            b_list.append(arr[i:j][:])
            r_list.append(arr[j:N][:])

    ru_max = 0
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

    ans = N*M - ru_max

    print(f'#{tc} {ans}')

# for tc in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     arr = [list(map(str, input().split())) for _ in range(N)]
#     ans = []
#     for i in range(1, N-1):
#         for j in range(i+1, N):
#             first = arr[0:i][:]
#             two = arr[i:j][:]
#             three = arr[j:N][:]
#
#             cnt_first = (a.count('W') for a in first)
#             cnt_two = (b.count('B') for b in two)
#             cnt_three = (c.count('R') for c in three)
#
#             result_first = len(first) * M - sum(cnt_first)
#             result_two = len(two) * M - sum(cnt_two)
#             result_three = len(three) * M - sum(cnt_three)
#
#             ans.append(result_first + result_two + result_three)
#
#         print(f'#{tc}', min(ans))

