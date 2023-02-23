'''
1
4
1 2 0 1
2 1 0 1
1 2 3 2
3 2 2 3
'''

# 델타를 사용해서 대각들의 합을 구할 것
# 기준점은 중복되지 않게 한 번만 더할 것
# 리스트에 담아 가장 큰 것을 뽑을 것
dr = [-1, 1, 1, -1]
dc = [-1, -1, 1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = []

    for r in range(N):
        for c in range(N):
            start = arr[r][c]
            result = 0
            for i in range(1, N):
                for dir in range(4):
                    nr, nc = r + dr[dir]*i, c + dc[dir]*i
                    if 0 <= nr < N and  0 <= nc < N:
                        result += arr[nr][nc]
            ans.append(start+result)

    print(max(ans))

