for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    air = [list(map(int, input().split())) for _ in range(M)]
    ans = N - 1
    print(ans)