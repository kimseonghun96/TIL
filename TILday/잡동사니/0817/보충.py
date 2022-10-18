# #파스칼 삼각형
# N = 5
# arr = [[0]*N for _ in range(N)]
#
# for i in range(N):
#     for j in range(0, i+1):
#         if j == 0 or i == j:
#             arr[i][j] = 1
#         else:
#             arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
#
# for line in arr:
#     print(*line)




#파스칼 다가가는 배경
# N = 5
# arr = [[0]*N for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         if i < j:
#             arr[i][j] = 1
#
# for line in arr:
#     print(*line)

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [[0]*N for _ in range(N)]   # N 상자 만듬
#
#     for i in range(N):
#         for j in range(0, i+1):
#             if j == 0 or i == j:      # 대각과 j가 0인 곳을
#                 arr[i][j] = 1         # 1로 채움
#
#             else:                     # 왼쪽 대각 위, 오른쪽 대각 위의 합을 저장
#                 arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
#
#
#     print(f'#{tc}')
#
#     for line in arr:  # 0 제거를 어떻게 하누..?
#         print(*line)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []   # 최종 담을 상자 상자 만듬

    for i in range(N):
        temp = [] # 임시 상자
        for j in range(0, i+1):
            if j == 0 or i == j:      # 대각과 j가 0인 곳을
                temp.append(1)        # 1로 채움

            else:
                temp.append(arr[i-1][j-1] + arr[i-1][j])  # 왼쪽 대각 위, 오른쪽 대각 위의 합을 저장
        arr.append(temp)   #최종적으로 합침

    print(f'#{tc}')

    for line in arr:
        print(*line)

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     result = []
#     for i in range(N):
#         temp = []
#         for j in range(i+1):
#             if j == 0 or j == i:
#                 temp.append(1)
#             else:
#                 temp.append(result[i-1][j] + result[i-1][j-1])
#         result.append(temp)
#
#     print(f'#{tc}')
#     for i in result:
#         print(*i)







