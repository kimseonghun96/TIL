import sys
sys.stdin = open('test_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input()))
    # print(num[1])
    max_len = 0

    temp = []
    for i in range(N):
        if num[i] == 1:
            temp.append(num[i])
        # print(temp)
        elif num[i] == 0:
            if max_len < len(temp):
                max_len = len(temp)
                temp =[]
    # print(temp)
    if num[-1] == 1:
        if max_len < len(temp):
            max_len = len(temp)

    print(f'#{tc} {max_len}')


