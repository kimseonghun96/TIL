import sys
sys.stdin = open('test_input.txt')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # print(arr)

    for r in range(N-M+1):
        for c in range(N-M+1):
            temp = []
            for i in range(M):
                for j in range(M):
                    temp.append(arr[i][j])
    max_die = 0
    for i in range(N):
        if sum(temp) > max_die:
            max_die = sum(temp)

    print(f'#{tc} {max_die}')

    # print(temp)










