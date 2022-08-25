import sys
sys.stdin = open('두개의 숫자열 input.txt')

T = int ( input () )
for tc in range ( 1, T + 1 ):
    N, M = map ( int, input ().split () )
    A = list ( input ().split () )  # 1차원 리스트 만듬
    B = list ( input ().split () )
    # print(list_A)
    max_num = []  # sum_num 들을  받고, 마지막에 솔트 한담에 -1꺼 뽑으면 될 듯?

    for i in range ( N ):
        sum = 0
        if len ( A ) == len ( B ):
            sum += (A[i] * B[i])
        max_num.append(sum)

    for i in range(M-N+1):
        sum = 0
        for j in range(len(A)):
            if len(A) < len(B):
                sum += A[j]*B[i]
            max_num.append(sum)

        else:
            sum += A[j]*B[i+j]
            max_num.append(sum)


    max_num = max_num.sort ()
    print ( f'#{tc} {max_num[-1]}' )














# T = int ( input () )
# for tc in range ( 1, T + 1 ):
#     N, M = map ( int, input ().split () )
#     A = list ( input ().split () )  # 1차원 리스트 만듬
#     B = list ( input ().split () )
#     # print(A)
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




