'''
1
3 7
***....
*-..#**
#<.****
23
SURSSSSUSLSRSSSURRDSRDS
'''
U = [-1, 0]
D = [1, 0]
L = [-1, 0]
R = [0, 1]



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    field = [list(input()) for _ in range(N)]
    str_line = int(input())
    game = list(input())

    for r in range(N):
        for c in range(M):
            if field[r][c] == '<' or '^' or 'v' or '>':
                start = field[r][c]

                if

