import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    n_case = list(map(int, input().split()))
    # print(n_case)
    last = n_case[-1] #가장 뒤의 값
    # print(n_case)
    result = 0
    for i in range(len(n_case)-1,-1,-1):
        if last > n_case[i]:
            result += last - n_case[i]
        else:
            last = n_case[i]


    print(f'#{tc} {result}')
