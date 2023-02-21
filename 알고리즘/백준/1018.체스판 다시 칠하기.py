'''
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
'''

n, m = map(int, input().split())

board = []
ans = []

for _ in range(n):
    board.append(input())

for i in range(n-7):
    for j in range(m-7):
        draw1 = 0   # 시작점 B
        draw2 = 0   # 시작점 W

        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a + b) % 2 == 0:
                    if board[a][b] != 'B':
                        draw1 += 1
                    else:
                        draw2 += 1
                else:
                    if board[a][b] != 'W':
                        draw1 += 1
                    else:
                        draw2 += 1

        ans.append(draw1)
        ans.append(draw2)

# print(ans)
print(min(ans))
