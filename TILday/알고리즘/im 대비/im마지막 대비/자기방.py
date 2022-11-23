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
    arr = [0] * 201
    for i in range(N):
        start, end = map(int, input().split())
        a = (start//2) + (start%2)
        b = (end//2) + (end%2)

        if a < b:
            for k in range(a, b+1):
                arr[k] += 1

        else:
            for k  in range(b, a+1):
                arr[k] += 1

    print(f'#{tc}', max(arr))


