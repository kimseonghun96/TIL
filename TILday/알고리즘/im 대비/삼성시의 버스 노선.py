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

# # 인덱스에 저장해서 개수 출력 하면 될 듯?
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     A1, B1 = map(int, input().split())
#     A2, B2 = map(int, input().split())
#     P = int(input())
#     for i in range(1, N+1):
#         cnt_list1 = [0] * (P+1)     # idx 저장할 빈 리스트
#         cnt_list2 = [0] * (P+1)
#         for j in range(A1, B1+1):      # 첫번째 범위를 보고 있으면 인덱스 1로 변경
#             cnt_list1[j] = 1
#         for j in range(A2, B2+1):      # 두번째 범위
#             if j:
#                 cnt_list2[j] += 1
#
#         cnt_idx = [0] * (P + 1)               # 두 리스트 합칠거
#         for k in range(len(cnt_idx)):
#             if cnt_list1[k]:
#                 cnt_idx[k] += 1
#             if cnt_list2[k]:
#                 cnt_idx[k] += 1
#
#         print(*cnt_idx)


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

# 인덱스에 저장해서 개수 출력 하면 될 듯?
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt_list = [0] * (5000 + 1)  # idx 저장할 빈 리스트
    for n in range(N):
        A, B = map(int, input().split())
        for i in range(A, B + 1):  # 첫번째 범위를 보고 있으면 인덱스 1 추가
            cnt_list[i] += 1
    P = int(input())   # 버스 정류장 개수
    ans = []
    for k in range(P):
        bus_stop = int(input()) # 버스 정류장 번호
        bus_stop_num = cnt_list[bus_stop] # 버스정류장 번호에 저장되어있는 노선수를 저장할 변수
        # print(bus_stop_num)
        ans.append(bus_stop_num)
        # for bus_stop in range(P+1):
        #     # if cnt_list[i] != 0:
        #     ans.append(cnt_list[bus_stop])

    print(f'#{tc}', *ans)


