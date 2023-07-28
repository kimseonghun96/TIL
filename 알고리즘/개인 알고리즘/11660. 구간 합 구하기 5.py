# 시간초과

# N, M = map(int, input().split())
#
# arr = []  # 2차원 배열
#
# for _ in range(N):
#     arr.append(list(map(int, input().split())))
#
# coordinates = []  # 좌표 값들을 모아둘 리스트
#
# for _ in range(M):
#     coordinates.append(list(map(int, input().split())))
#
# for coord in coordinates:
#     x1, y1, x2, y2 = coord
#     ans = 0
#     for i in range(x1 - 1, x2):
#         for j in range(y1 - 1, y2):
#             ans += arr[i][j]
#     print(ans)



# N, M = map(int, input().split())
#
# arr = []  # 2차원 배열
# prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]  # 누적 합 배열
#
# for _ in range(N):
#     row = list(map(int, input().split()))
#     arr.append(row)
#
# # 누적 합 배열 계산
# for i in range(1, N + 1):
#     for j in range(1, N + 1):
#         prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + arr[i - 1][j - 1]
#
# # 좌표 구간의 합 계산
# for _ in range(M):
#     x1, y1, x2, y2 = map(int, input().split())
#     ans = prefix_sum[x2][y2] - prefix_sum[x1 - 1][y2] - prefix_sum[x2][y1 - 1] + prefix_sum[x1 - 1][y1 - 1]
#     print(ans)


import sys

N, M = map(int, sys.stdin.readline().split())

arr = []  # 2차원 배열
prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]  # 누적 합 배열

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

# 누적 합 배열 계산
for i in range(1, N + 1):
    for j in range(1, N + 1):
        prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + arr[i - 1][j - 1]

# 좌표 구간의 합 계산
for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    ans = prefix_sum[x2][y2] - prefix_sum[x1 - 1][y2] - prefix_sum[x2][y1 - 1] + prefix_sum[x1 - 1][y1 - 1]
    print(ans)
