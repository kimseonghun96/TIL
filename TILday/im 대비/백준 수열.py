'''
9
1 2 2 4 4 5 7 7 2
바로 이전의 수를 기억하고 현재 수가 이전의 수보다 큰 경우, 작은 경우를 나누어 연속한 횟수를 센다.
수를 셀 때마다 연속한 최대 횟수를 세 갱신해준뒤 마지막에 출력하면 된다.
'''
# N = int(input())
# arr = list(map(int, input().split()))
#
# start = arr[0]
# cnt = 1
# for i in arr[1:]:
#     temp = 1
#     if start <= i:
#         temp += i
#         start = i
#
#     else:
#         if cnt < max(temp):
#             cnt = max(temp)
# print(cnt)
#
#
# pa_arr = arr[::-1]
# # print(sort_arr)
# pa_start = pa_arr[0]
# for i in arr[1:]:
#     temp = 1
#     if pa_start <= i:
#         temp += 1
#         pa_start = i
#     else:
#         if cnt < temp:
#             cnt = temp
#             break
#
#
# print(cnt)

n = int(input())
arr = list(map(int,input().split()))
prev = arr[0]
min_cnt = 1
max_cnt = 1
ans = 1

for i in arr[1:]:
    if i >= prev:
        min_cnt += 1
    else:
        min_cnt = 1

    if i <= prev:
        max_cnt += 1
    else:
        max_cnt = 1
    prev = i

    # print(min_cnt)       # 여러개가 있네..?

    ans = max(ans, min_cnt, max_cnt)
print(ans)