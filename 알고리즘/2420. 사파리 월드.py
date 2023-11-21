n, m = map(int, input().split())


if m < 0 and n < 0:
    m, n = abs(m), abs(n)
    ans = [n, m]
    print(max(ans) - min(ans))

else:
    ans = [n, m]
    print(max(ans) - min(ans))