'''
import sys
sys.stdin = open('보충input.txt')

T = 10
for tc in range(1, T + 1):
    tc_num = input()
    arr = []
    for i in range(100):
        temp = list(map(int, input().split()))

    # [list(map(int, input().split())) for _ in range(100)]
    # 행의 합 구하기
    max_sum = 0  # 계산 되는 합 보다 작은 수를 설정해야지 첫번째 비교했을 때 그 값이 저장됨(무조건 첫번째 비교 값을 저장하기 위해)
    for i in range(100):
        row_sum = 0  # 각 행의 시작할 때 초기화하는 변수 만듬 포문 안에 넣으면 저기를 지나갈때 초기화 되기때문에 합이 더해지지 않음
        for j in range(100):
            row_sum += arr[i][j]  # arr[i]의 행의 합이 row_sum에 저장된 상태
        if max_sum < row_sum:
            max_sum = row_sum
    # 열의 합 구하기

    for i in range(100):  # 열을 먼저 선택
        col_sum = 0
        for j in range(100):
            col_sum += arr[i][j]
        if max_sum < col_sum:
            max_sum = col_sum

    # 대각합 구하기
    gak_sum = 0
    for i in range(100):
        gak_sum += arr[i][i]
    if max_sum < gak_sum:
        max_sum = gak_sum

    gak_sum = 0
    for i in range(100):
        gak_sum += arr[i][100 - 1 - i]
    if max_sum < gak_sum:
        max_sum = gak_sum

    print(f'#{tc} {max_sum}')
'''

#답..
import sys
sys.stdin = open('보충input.txt')

T = 10
for tc in range(1, T + 1):
    tc_num = input()
    arr = []
    for i in range(100):
        temp = list(map(int, input().split()))
        arr.append(temp)
    # [list(map(int, input().split())) for _ in range(100)]

    max_sum = 0  # 아주 작은값
    for i in range(100):
        row_sum = 0  # 각 행의 시작시 초기화
        for j in range(100):
            row_sum += arr[i][j]
        # arr[i] 행의 합이 row_sum 저장된 상태
        if max_sum < row_sum:
            max_sum = row_sum

    # 열의 합 구하기
    for i in range(100): # 열을 먼저 선택
        col_sum = 0
        for j in range(100): # 행
            col_sum += arr[j][i]
        if max_sum < col_sum:
            max_sum = col_sum

    # 대각 합 구하기
    gak_sum = 0
    for i in range(100):
        gak_sum += arr[i][i]
    if max_sum < gak_sum:
        max_sum = gak_sum

    gak_sum = 0
    for i in range(100):
        gak_sum += arr[i][100 - 1 - i]
    if max_sum < gak_sum:
        max_sum = gak_sum

    print(f'#{tc} {max_sum}')