import sys
sys.stdin = open('두개의 숫자열 input.txt')

# A와 B의 요소를 곱한 값을 하나의 리스트에 모으고 솔트를 사용해
# 가장 큰 수를 [-1]자리로 옮기고 출력

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # print(A)

    if N == M:                      # N과 M이 같을 때
        max = 0                     # 최대값 변수
        for i in range(N):          # 작은 범위를 기준으로(같으므로 상관 x)
            max += A[i] * B[i]      # max에 추가

    else:                               # 반대경우 N과 M이 다를 때
        if N > M:                       # N이 M보다 클 때
            sum = [0] * (N - M + 1)     # N - M의 범위를 비교 하기 위해 +1
            for i in range(len(sum)):
                for j in range(-1, -M - 1, -1):
                    sum[i] += A[j - i] * B[j]
        else:
            sum = [0] * (M - N + 1)
            for i in range(len(sum)):
                for j in range(-1, -N - 1, -1):
                    sum[i] += A[j] * B[j - i]
        # print(sum)
        sum.sort()
        max = sum[-1]

    print(f'#{tc} {max}')



print('===============================================================================================================')

import sys
sys.stdin = open('두개의 숫자열 input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # print(A)

    if N == M:                      # N과 M이 같을 때
        max = 0                     # 최대값 변수
        for i in range(N):          # 작은 범위를 기준으로(같으므로 상관 x)
            max += A[i] * B[i]      # max에 추가

    else:                               # 반대경우 N과 M이 다를 때
        if N > M:                       # N이 M보다 클 때
            sum = [0] * (N - M + 1)     # N - M의 범위를 비교 하기 위해 +1
            for i in range(len(sum)):
                for j in range(M):      # 작은거 기준
                    sum[i] += A[j + i] * B[j]
        else:
            sum = [0] * (M - N + 1)
            for i in range(len(sum)):
                for j in range(N):      # 작은거 기준
                    sum[i] += A[j] * B[j + i]
        # print(sum)
        sum.sort()
        max = sum[-1]

    print(f'#{tc} {max}')







# T = int ( input () )
# for tc in range ( 1, T + 1 ):
#     N, M = map ( int, input ().split () )
#     A = list ( input ().split () )  # 1차원 리스트 만듬
#     B = list ( input ().split () )
    # print(A)
#     max_num = []  # sum_num 들을  받고, 마지막에 솔트 한담에 -1꺼 뽑으면 될 듯?
#
#     for i in range ( len ( B ) - len ( A ) + 1 ):
#         multiple_num = 0
#         for j in range ( len ( A ) ):
#             if len ( A ) < len ( B ):
#                 A[i] * B ( i ) = multiple_num
#                 max_num += multiple_num
#
#             elif len ( A ) > len ( B ):
#                 A[i] * B[i + j] = multiple_num
#                 max_num += multiple_num
#
#             elif len ( A ) == len ( B ):
#                 A[j] * B[j] = multiple_num
#                 max_num += multiple_num


# T = int(input())
# for tc in range(1, T+1):
#     N , M = map(int, input().split())
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
#
#     #for 문을 돌릴 i 값은
#     # ex) N, M이 2, 3 일 경우 2가지, 3, 5일 경우 4가지
#
#     result = 0
#     for i in range(abs(N-M)+1):   # N M 어떤게 더 클지 모르니 절댓값을 씌워준다
#         value = 0
#         for j in range(min(N, M)):
#             if N > M :
#                 value += A[j+i] * B[j]
#             elif N < M :
#                 value += A[j] * B[j+i]
#             elif N == M :
#                 value += A[j] * B[j]
#
#         if value > result :
#             result = value
#
#     print(f'#{tc} {result}')



