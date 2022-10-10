T = int(input())                                # 테스트 횟수 입력

for t in range(1, T+1):
    N = int(input())
    card_list = list(map(int, input()))
    cnt_list = [0] * 10

    for card_num in card_list:
        cnt_list[card_num] += 1

    max_card = 0
    how_many = 0

    for idx in range(10):
        if cnt_list[idx] == 0:
            continue

        else:
            if how_many <= cnt_list[idx]:
                how_many = cnt_list[idx]
                max_card = idx

    print(f'#{t} {max_card} {how_many}')


# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     num = int(input())
#
#     num_list = []
#     for i in range(N):
#         if num % 10 == 0:
#             num_list.append(0)
#         elif num % 10 != 0:
#             num_list.append(num % 10)
#             num = num//10
#     # print(num_list)
#     idx_box = [0] * 101
#     for i in range(N):
#         idx_box[num_list[i]] += 1
#
#     max_cnt = 0
#     for i in range(len(idx_box)):
#         if idx_box[i] == max(idx_box):
#             if max_cnt < i:
#                 max_cnt = i
#
#     print(f'#{tc}', max_cnt, max(idx_box))

