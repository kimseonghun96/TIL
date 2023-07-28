import sys

N = int(sys.stdin.readline())
num_list = sorted(list(map(int, sys.stdin.readline().split()))) # 이 카드에

M = int(sys.stdin.readline())
checks_num = list(map(int, sys.stdin.readline().split())) # 이 숫자들이 있는지 없는지 확인 해야함

for check in checks_num:
    start, end = 0, N-1  # 인덱스
    exist = False
    while start <= end:
        mid = (start + end) // 2
        # checks_num 안의 값(check)들을 num_list 중간에 있는 값이랑 비교해서
        # 시작과 끝점을 계속 바꿔줌
        # 똑같은 값이 있다면 exist 상태를 1로 바꾸고 출력
        # 없다면 exist 상태를 바꾸지 않고 0출력
        if check > num_list[mid]:
            start = mid + 1
        elif check < num_list[mid]:
            end = mid - 1
        else:
            exist = True
            break

    if exist == False:
        print(0, end= ' ')
    else:
        print(1, end= ' ')




