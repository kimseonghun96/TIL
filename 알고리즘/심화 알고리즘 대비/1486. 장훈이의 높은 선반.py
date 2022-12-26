'''
1
5 16
1 3 3 5 6
'''


# def recur(depth, visited, ans):
#     global sum_tall
#     visited = set(visited)
#     sum_tall.add(ans)
#
#     if depth == N:
#         return
#     for i in range(len(tall)):
#         if i not in visited:
#             visited.add(i)
#             recur(depth+1, visited, ans+tall[i])
#             visited.remove(i)
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, B = map(int, input().split())
#     tall = list(map(int, input().split()))
#     result = []
#     sum_tall = set()
#     recur(0, set(), 0)
#     ssum_tall = list(sum_tall)
#
#     for j in range(len(sum_tall)):
#         if ssum_tall[j] >= B:
#             result.append(ssum_tall[j])
#
#     print(f'#{tc} {min(result) - B}')
#     # print(tall)
#     # print(ssum_tall)
#     # print(sum_tall)





# ------------------------------------------------------------------------------------------------
# def recur(depth, visited, temp_sum):
#     global sum_tall
#     visited = set(visited)
#     if depth > N:
#         sum_tall.add(temp_sum)
#     else:
#         if B <= temp_sum:
#             sum_tall.add(temp_sum)
#         for i in range(len(tall)):
#             if i not in visited:
#                 visited.add(i)
#                 recur(depth+1, visited, temp_sum+tall[i])
#                 visited.remove(i)
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, B = tuple(map(int, input().split()))
#     tall = list(map(int, input().split()))
#     ans = 999999999999999
#     # result = []
#     sum_tall = set()
#     recur(0, set(), 0)
#     print(f'#{tc} {min(sum_tall) - B}')
    # print(tall)
    # print(ssum_tall)
    # print(ssum_tall)



def recur(depth, visited, temp_sum):
    global ans
    visited = set(visited)
    if depth > N:
        return
    else:
        if B <= temp_sum:
            if ans > temp_sum - B:
                ans = temp_sum - B
        for i in range(len(tall)):
            if i not in visited:
                visited.add(i)
                recur(depth+1, visited, temp_sum+tall[i])
                visited.remove(i)


T = int(input())
for tc in range(1, T+1):
    N, B = tuple(map(int, input().split()))
    tall = list(map(int, input().split()))
    ans = 999999999999999
    # result = []
    sum_tall = set()
    recur(0, set(), 0)
    print(f'#{tc} {ans}')
