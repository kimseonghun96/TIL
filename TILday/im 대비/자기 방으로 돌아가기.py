# 두개의 박스
# 시작 점을 고르고 포문을 변의 길이 만큼 추가 해주고
# 그 리스트를 다담아서 더 함
'''
1
4 1
0 2 1 3
1 0 0 1
2 0 2 0
3 2 2 2
1 0 2
'''
T = int(input())
for tc in range(1, T+1):
    N, small_box = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    i, j, n = map(int, input().split())
    ans = 0
    start = arr[i][j]
    for r in range(N):
        for c in range(N):
            ans += arr[i+n][j+n]

    print(ans)