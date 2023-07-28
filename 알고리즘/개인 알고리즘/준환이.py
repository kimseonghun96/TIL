'''
3
300 400 240
300 400 350
300 400 480
gdgdgdgdg
'''

T = int(input())
for tc in range(1, T+1):
    L, U, X = map(int, input().split())

    if X <= U and X >= L:
        ans = 0

    elif X < L:
        ans = L - X

    else:
        ans = -1

    print(ans)