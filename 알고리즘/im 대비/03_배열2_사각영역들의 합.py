# 큰 박스 안에서 먼저 작은 박스 한개의 범위를 구하고 그 합을 구한다
# 합을 더한 공간은 0으로 만들고
# 두 번째 작은 박스 범위 안에 있는 숫자의 합을 구한다.

'''
3
4 1
0 2 1 3
1 0 0 1
2 0 2 0
3 2 2 2
1 0 2
4 2
3 2 0 3
3 0 3 0
1 0 0 2
0 3 3 3
2 1 2
0 1 2
5 2
2 4 3 1 3
4 0 2 3 2
2 0 3 4 3
1 3 4 3 1
3 0 3 3 4
1 2 2
2 3 3

'''
T = int(input())
for tc in range(1, T+1):
    N, small_box = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for _ in range(small_box):
        r, c, n = map(int, input().split())
        for i in range(N):
            for j in range(N):
                for t in range(n):
                    for k in range(n):
                        if 0 <= r+t < N and 0 <= c+k < N:
                            ans += arr[r+t][c+k]
                            arr[r+t][c+k] = 0


    print(f'#{tc} {ans}')