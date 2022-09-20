'''
2
2
1 2
3 4
3
9 3 4
6 1 5
7 8 2
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    max_list = []   # 가장 길게 이동 한 시작점
    max_cnt = -1    # 가장 길게 이동한 거리
    for i in range(N):
        for j in range(N):
            start = [i, j]
            stack = [start]
            cnt = 1

    # print(stack)
            #   dfs + 델타
            while stack:
                current = stack.pop()

                for k in range(4):
                    ni = current[0] + di[k]
                    nj = current[1] + dj[k]

                    # 범위 설정
                    # 현재위치와 이동할 방의 차가 1이면
                    # cnt +1
                    if 0 <= ni < N and 0 <= nj < N:
                        if arr[ni][nj] - arr[current[0]][current[1]] == 1:
                            stack.append([ni, nj])
                            cnt += 1

            # 만약 현재 이동거리가 최대 이동거리보다 길다면,
            if cnt > max_cnt:
                max_cnt = cnt
                max_list = [arr[i][j]]

            # 만약 현재 이동거리가 최대 이동거리라면
            elif cnt == max_cnt:
                max_list.append(arr[i][j])

    print(f'#{tc} {min(max_list)} {max_cnt}')



