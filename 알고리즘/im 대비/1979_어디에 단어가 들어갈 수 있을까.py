import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    word_box = 0

    for r in range(N):
        cnt = 0
        for c in range(N):
            if arr[r][c] == 1:
                cnt += 1
            if arr[r][c] == 0 or c == N-1:
                if cnt == K:
                    word_box += 1

                if arr[r][c] == 0:
                    cnt = 0
                # else:
                #     cnt = 0

    for r in range(N):
        cnt = 0
        for c in range(N):
            if arr[c][r] == 1:
                cnt += 1
            if arr[c][r] == 0 or c == N-1:
                if cnt == K:
                    word_box += 1

                if arr[c][r] == 0:
                    cnt = 0
                # else:
                #     cnt = 0


    print(f'#{tc} {word_box}')
































'''
1. 각 테스트 케이스마다 n과 k를 입력받고, 퍼즐의 상태를 입력받아 data 리스트를 정의한다.

 

2. result를 0으로 초기화 한 뒤, 가장 먼저 가로의 상황을 확인한다. 해당 작업 과정은 아래와 같다.

  - 2중 for문을 통해 data 리스트 요소를 하나씩 확인하며, 해당 값이 1일 경우 cnt를 1 증가 시킨다.

  - 만약 현재의 값이 0이거나 마지막 열일 경우 cnt 값을 확인하고 cnt 값이 k와 같을 경우 result를 1 증가 시킨다.

  - 이후 현재의 값이 0일 경우 cnt를 다시 0으로 초기화한다.

 

3. 가로의 상황을 확인한 뒤 세로의 상황을 확인한다. 해당 작업 과정은 아래와 같다.

  - 2중 for문을 통해 data 리스트 요소를 하나씩 확인하며, 해당 값이 1일 경우 cnt를 1 증가 시킨다.

  - 만약 현재의 값이 0이거나 마지막 행일 경우 cnt 값을 확인하고 cnt 값이 k와 같을 경우 result를 1 증가 시킨다.

  - 이후 현재의 값이 0일 경우 cnt를 다시 0으로 초기화한다.

 

4. 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.
'''

# for tc in range ( 1, t + 1 ):
#     n, k = map ( int, input ().split () )
#     data = [list ( map ( int, input ().split () ) ) for _ in range ( n )]
#
#     result = 0
#     # 가로 확인
#     for i in range ( n ):
#         cnt = 0
#         for j in range ( n ):
#             if data[i][j] == 1:
#                 cnt += 1
#             if data[i][j] == 0 or j == n - 1:
#                 if cnt == k:
#                     result += 1
#                 if data[i][j] == 0:
#                     cnt = 0
#
#     # 세로 확인
#     for i in range ( n ):
#         cnt = 0
#         for j in range ( n ):
#             if data[j][i] == 1:
#                 cnt += 1
#             if data[j][i] == 0 or j == n - 1:
#                 if cnt == k:
#                     result += 1
#                 if data[j][i] == 0:
#                     cnt = 0
#
#     print ( '#%d %d' % (tc, result) )
