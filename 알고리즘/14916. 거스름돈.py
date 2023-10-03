# 가장 큰 거에서 하나씩 제외해나가는거

n = int(input())

ans = 0

if n % 5 == 0:
    ans = n // 5
else:
    for i in range(n//5, -1, -1):
        change = n - i*5
        if change % 2 == 0:
            ans += i
            ans += change // 2
            break

if ans == 0:
    print(-1)
else:
    print(ans)