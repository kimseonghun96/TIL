T = int(input())
for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    last = price[-1]
    # 가장 뒤의 값을 담고
    # 뒤에서 부터 포문을 돌면서
    # 크기 비교 뒤의 것보다 앞의 것이 작다면
    # 차이를 ans에 더하고
    # 앞의 것이 더 크다면 그 값을 last에 저장띠

    ans = 0
    for i in range(len(price)-1, -1, -1):
        if last > price[i]:
            ans += last - price[i]
        else:
            last = price[i]

    print(f'#{tc} {ans}')

