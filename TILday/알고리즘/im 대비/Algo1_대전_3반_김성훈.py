# 완전 탐색을 하면서 다트가 맞은 곳을 먼저 더하고
# 맞은 곳부터 상하좌우 1칸식을 더한다. 그 값을 temp에 저장
# ans를 0으로 설정하고 포문의 마지막에 ans와 temp의 값을 비교해서
# temp의 값이 더 크다면 ans를 temp값으로 변경한다.

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for r in range(N):
        for c in range(N):
            temp = arr[r][c]            # 다트가 맞은 지점을 먼저 temp에 저장
            for k in range(4):
                for t in range(1, 2):   # 다트가 맞은 지점을 제외한 상하좌우 한칸씩을 볼 것이다.
                    nr, nc = r + dr[k] * t, c + dc[k] * t
                    if 0 <= nr < N and 0 <= nc < N:     # 범위를 넘지 않는다면.
                        temp += arr[nr][nc]     # 상하좌우도 더해 준다.
            if temp > ans:      # 최대 합계의 점수를 얻기 위해서 tmep에 저장된 값이 ans값 보다 크다면
                ans = temp      # temp의 값을 ans값으로 바꿔준다.

    print(f'#{tc} {ans}')

























