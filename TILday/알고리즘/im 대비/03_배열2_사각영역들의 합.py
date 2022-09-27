# 두개의 박스
# 시작 점을 고르고 포문을 변의 길이 만큼 추가 해주고
# 그 리스트를 다담아서 더 함
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
    i, j, n = map(int, input().split())  # 시작점이 고정이 되면 안됨 이거 포문안에 드러가야됨
    ans = 0
    start = arr[i][j]
    for t in range(small_box):
        temp = []
        for r in range(n):
            for c in range(n):
                if i+r < N and j+c < N:
                    temp.append(arr[i+r][j+c])
        print(temp)

    print(f'#{tc} {ans}')