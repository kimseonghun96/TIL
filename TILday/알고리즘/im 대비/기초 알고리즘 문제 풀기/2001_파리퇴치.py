import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    answer = 0          # 최대값
    for r in range(N-M+1):                  # 2칸식 비교하려면 4번 봐야된다
        for c in range(N-M+1):
            sum_arr = 0                     # 작은 상자 합 더할거
            for i in range(M):
                for j in range(M):
                    sum_arr += arr[r+i][c+j]       # 작은 범위의 합을 구해야됨
                    # print(sum_arr)
                    if answer < sum_arr:
                        answer = sum_arr
    # print(answer)

    print(f'#{tc} {answer}')






