import sys
sys.stdin = open('test_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = 0
    for r in range(N-M+1):
        for c in range(N-M+1):
            value = 0
            for i in range(M):
                for j in range(M):
                    value += arr[r+i][c+j]
                    if answer < value:
                        answer = value

    print(f'#{tc} {answer}')

