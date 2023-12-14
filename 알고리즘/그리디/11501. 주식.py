T = int(input())
for _ in range(T):
    N = int(input())
    stock = list(map(int, input().split()))
    stock.reverse() # 뒤집기 ㅎㅎ
    max = stock[0]
    ans = 0

    for i in range(1, N):
        if max < stock[i]:
            max = stock[i]
            continue
        ans += max - stock[i]

    print(ans)