# 뭔가 이렇게 푸는 거 아닌 거 같은데..
# 분무기가 있는 곳에서 3일 경우 자신 포함 7칸을 채우는 거니까
# 7 만큼 나누고 딱떨어지면 그 값이 답, 떨어지지 않는 다면 7이하의 칸을 더 채워줘야되니까 + 1
T = int(input())
for tc in range(1, T+1):
    N, D = map(int, input().split())
    ans = 0
    if N % (2 * D + 1) == 0:
        ans = N // (2 * D + 1)
    else:
        ans = N // (2 * D + 1) + 1

    print(f'#{tc} {ans}')