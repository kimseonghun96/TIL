# 2차원 배열 안에서 파리가 죽는 범위를 모두 비교 한다.

'''
2
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3
6 3
29 21 26 9 5 8
21 19 8 0 21 19
9 24 2 11 4 24
19 29 1 0 21 19
10 29 6 18 4 3
29 11 15 3 3 29
'''

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0  # 가장 많이 죽은 파리를 구할 값

    for i in range(N-M+1):
        for j in range(N-M+1):
            temp = 0   # 한번 내리칠 때 죽은 파리의 수
            for r in range(i, i+M):
                for c in range(j, j+M):
                    temp += arr[r][c]
            if ans < temp:
                ans = temp

    print(f'#{tc} {ans}')

