#부분집합 이론
T = int(input())
for tc in range(1, T+1):
    num = list(map(int, input().split()))
    num_sum_zero = 0

    for i in range(1, 1 << 10):
        num_sub = []
        for j in range(10):  # 가야하는 길이는 10
            if i & (1 << j):  # 1칸씩 왼쪽으로 옮겨가며 총 10칸을 대조해본다.
                num_sub.append(num[j])  # 부분집합을 구했음

        total = 0           # 총 길이 초기화

        for k in num_sub:
            total += k      #부분집합의 합을 total에 추가

            if total == 0:       # total이 0이라면
                num_sum_zero= 1  # num_sum_zero에 1을 넣고 멈춤
                break
    print(f'#{tc} {num_sum_zero}')

#실습
#4837. [파이썬 S/W 문제해결 기본] 2일차 - 부분집합의 합
T = int(input())
for tc in range(1, T+1):
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    N, K = map(int, input().split())  #N, K 를 입력 받을 곳
    result = 0

    for i in range(1, 1 << len(A)):
        sub_list = []
        length = 0  # 길이 초기값 설정
        for j in range(len(A)):  # 가야하는 길이는
            if i & (1 << j):  # 1칸씩 왼쪽으로 옮겨가며 총 칸을 대조해본다.
                sub_list.append(A[j])  # 부분집합을 구했음
                length += 1

        if length == N:  # 길이와  입력받은 N의 길이가 같다면.
            sum_list = 0
            for k in range(length):
                sum_list += sub_list[k]  # 부분집합의 합을 sum_list에 추가

            if sum_list == K:  # sum_list의 값이 K와 같으면
                result += 1    # result에 1을 추가

    print(f'#{tc} {result}')