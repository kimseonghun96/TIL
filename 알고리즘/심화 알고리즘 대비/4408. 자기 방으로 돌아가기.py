'''
1
4
10 100
20 80
30 50
11 41
'''
# 복도에 홀수와 짝수를 모으는 방법을 생각해야된다.
# 이동하는 방이 더 작은 방으로 이동 할 수도 있음..


for tc in range(1, int(input())+1):
    N = int(input())
    board = [0] * 201

    for i in range(N):
        now, back = map(int, input().split())
        now = (now // 2) + (now % 2)
        back = (back // 2) + (back % 2)
        if back > now:
            for t in range(now, back+1):
                board[t] += 1

        else:
            for t in range(back, now+1):
                board[t] += 1

    print(f'#{tc}', max(board))




# for tc in range(1, int(input())+1):
#     N = int(input())
#     board_1 = [0] * 401     # 홀
#     board_2 = [0] * 401     # 짝
#     for i in range(N):
#         now, back = map(int, input().split())
#         if back > now:
#             for t in range(now, back+1):
#                 if now % 2 == 0:
#                     board_2[t] += 1
#             for t in range(now, back+1):
#                 if now % 2 == 1:
#                     board_1[t] += 1
#
#         else:
#             for t in range(back, now+1):
#                 if back % 2 == 0:
#                     board_2[t] += 1
#             for t in range(back, now+1):
#                 if back % 2 == 1:
#                     board_1[t] += 1
#
#
#     # print(board_1)
#     # print(board_2)
#
#     for i in range(401):
#         board_1[i] = board_1[i] + board_2[i]
#     # print(board_1)
#     print(f'#{tc}', max(board_1))



















    # for k in range(len(temp) -3):
    #     if temp[k+3] < temp[k] and temp[k+1] > temp[k+2]:
    #         ans = 1
    #         k += 1
    #     elif temp[k] < temp[k+3] and temp[k+2] > temp[k+1]:
    #         ans = 1
    #         k += 1
    #
    #     elif temp[k] <= temp[k + 3] <= temp[k + 1] or temp[k] <= temp[k + 2] <= temp[k + 1]:
    #         ans += 1
    #         k += 1
    #
    #     elif temp[k+2] - temp[k] == 1 or temp[k] - temp[k+2] == 1:
    #         ans += 1
    #         k += 1


    # print(f'#{tc} {ans}')



