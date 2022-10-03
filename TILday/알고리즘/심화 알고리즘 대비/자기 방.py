'''
3
4
10 20
30 40
50 60
70 80
2
1 3
2 200
3
10 100
20 80
30 50
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [0] * 201
    for _ in range(N):
        room1, room2 = map(int, input().split())
        a,b = (room1//2 + room1 % 2), (room2//2 + room2 % 2)
        if room2 > room1:
            for i in range(a, b+1):
                board[i] += 1
        elif room2 < room1:
            for i in range(b, a+1):
                board[i] += 1

    print(f'#{tc}', max(board))