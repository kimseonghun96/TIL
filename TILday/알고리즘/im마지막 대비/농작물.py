# 각 줄마다 맞는 조건을 설정하며 합을 구한다.

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        arr = list(map(int, input()))
        if i == 0:                                                  # 첫번째 줄 중간 값
            ans += arr[N // 2]

        elif i < N // 2:
            ans += sum(arr[N // 2 - i:N // 2 + i + 1])              # 중간 줄 전까지 점점 늘어나는거

        elif i == N // 2:                                           # 중간 줄 다 더하고
            ans += sum(arr)

        elif N // 2 < i < N - 1:                                    # 중간 줄 이후부터 줄어드는거
            ans += sum(arr[i - N // 2:N - (i - N // 2)])
        # print(ans)
        elif N - 1 == i:                                            # 마지막줄 중간값
            ans += arr[N // 2]

    print(f'#{tc} {ans}')