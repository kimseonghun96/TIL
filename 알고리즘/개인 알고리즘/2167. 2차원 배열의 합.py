import sys

N, M = map(int, input().split())

arr = []

# 원 배열을 만든다.
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

K = int(input())

for _ in range(K):
    # 첨시작 좌표와 끝 좌표를 추출하고
    check_num = list(map(int, sys.stdin.readline().split()))
    start_pos = [check_num[0] -1, check_num[1] -1] # 인덱스 값을 0부터 시작하는 걸로 변경
    end_pos = [check_num[2] - 1, check_num[3] -1]

    # 그 좌표 값만큼만 비교해서 안의 값을 다 더함
    total_sum = 0
    for i in range(start_pos[0], end_pos[0] + 1):
        for j in range(start_pos[1], end_pos[1] + 1):
            total_sum += arr[i][j]

    print(total_sum)

###다른 방식
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
K = int(input())

for _ in range(K):
    ans = 0
    i, j, x, y = map(int, input().split())
    for t in range(i-1, x):
        for v in range(j-1, y):
            ans += arr[t][v]

    print(ans)





