'''
3
2
2 2 4 4 1
3 3 6 6 2
3
1 2 3 3 1
3 6 6 8 1
2 3 5 6 2
3
1 4 8 5 1
1 8 3 9 1
3 2 5 8 2
'''
# 상자1은 1로 채우고 상자 2는 2로 로 채우 고 더함
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*11 for _ in range(11)]
    num = 3
    for i in range(1, N+1):
        r, c, r2, c2, M = map(int, input().split())
        for k in range(r+1, r2+2):
            for t in range(c+1, c2+2):
                arr[k][t] += M
        # temp = temp + 1

    # print(num)
    cnt = 0
    for i in range(11):
        for j in range(11):
            if arr[i][j] == num:
                cnt +=1

    print(f'#{tc} {cnt}')
    # for line in arr:
    #     print(*line)


















