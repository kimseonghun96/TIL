n, m = map(int, input().split())

ansn = list(map(int, input().split()))
ansm = list(map(int, input().split()))

print(*sorted(ansn + ansm))


