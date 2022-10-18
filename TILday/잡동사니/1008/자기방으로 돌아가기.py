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
    line = [0] * 201
    for i in range(N):
        A, B = map(int, input().split())
        a, b = 0, 0
        if A % 2 == 0:
            a = A // 2
        else:
            a = (A // 2) + 1

        if B % 2 == 0:
            b = B // 2
        else:
            b = (B // 2) + 1

        if a < b:
            for k in range(a, b+1):
                line[k] += 1

        elif a > b:
            for k in range(b, a+1):
                line[k] += 1


    print(f'#{tc}', max(line))

#---------------------------------------
# for i in range(N):
#     now, back = map(int, input().split())
#     now = (now // 2) + (now % 2)
#     back = (back // 2) + (back % 2)
#     if back > now:
#         for t in range(now, back + 1):
#             board[t] += 1

