import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    list = [0] * 8

    for i in range(8):
        if N//money[i] != 0:            # 몫이 0이 아닐 경우
            list[i] = N//money[i]       # list[i]에 몫 추가
            N = N % money[i]            # N을 나머지로 바꾸고 포문 반복

    print(f'#{tc}')
    print(*list)

