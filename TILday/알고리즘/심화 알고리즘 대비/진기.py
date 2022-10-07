'''
4
2 2 2
3 4
2 2 2
1 2
2 2 1
4 2
2 2 1
3 2
'''
# T = int(input())
# for tc in range(1, T+1):
#     N, M, K = map(int, input().split())     # 사람 , 초, 붕어빵
#     jul = list(map(int, input().split()))
#
#     jul.sort()
#
#     ans = 'Possible'
#     for i in range(N):
#         if (jul[i]//M)*K < i+1:
#             ans = 'Impossible'
#             break
#
#     print(f'#{tc} {ans}')

'''
4
2 2 2
3 4
2 2 2
1 2
2 2 1
4 2
2 2 1
3 2
'''
# T = int(input())
# for tc in range(1, T+1):
#     N, M, K = map(int, input().split())     # 사람 , 초, 붕어빵
#     jul = list(map(int, input().split()))
#
#     jul.sort()
#
#     ans = 'Possible'
#     for i in range(N):
#         if (jul[i]//M)*K < i+1:
#             ans = 'Impossible'
#             break
#
#     print(f'#{tc} {ans}')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    time = list(map(int, input().split()))

    total = 0
    ans = 'Possible'
    time.sort()

    for i in range(0, N+1):  # N+1 과 11111+1의 차이?
        if i != 0 and i % M == 0:  # 붕어빵 개수 체크
            total += K

        if i in time:               # 손님이 오는 초에
            if total <= 0:          # 붕어빵이 없음
                ans = 'Impossible'  # 불가능
                break

            else:					# 붕어빵 있으면
                total -= 1		  # 한 개 주기

    print(f'#{tc} {ans}')


