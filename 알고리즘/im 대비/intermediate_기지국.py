import sys
sys.stdin = open('기지국input.txt')
# 기지국의 상하좌우를 X로 바꾼다음에 남은 집의 수를 카운트
T = int(input())
for tc in range(1, T+1):
    N = int(input())                            # 테케 받으려면 뭐해야되는지?
    MAP = [list(input()) for _ in range(N)]     # 문자 그대로 받으면 변경을 못하기 때문에 리스트로 받음
    dr = [-1, 1, 0, 0]          # 상, 하
    dc = [0, 0, -1, 1]          # 좌, 우
    # MAP[0][0] = 'X'                             # 이거 왜하는 거임?
    len_dict = {'A' : 1, 'B' : 2, 'C': 3}
    for r in range(N):
        for c in range(N):
            if MAP[r][c] == 'X' or MAP[r][c] == 'H':
                continue        # X or H인 경우 뛰어 넘음
            # K = 0
            # if MAP[r][c] == 'A':
            #     K = 1
            # elif MAP[r][c] == 'B'
            #     k = 2
            # else: K = 3
            K = len_dict[MAP[r][c]]

            for i in range(4):
                for j in range(1, K + 1):  # 중간점은 따로 찍고, 반복을 최대치로 해주고 나중에 끊을 거임
                    # (r, c) => 4방향 좌표를 생성
                    nr = r + dr[i] * j
                    nc = c + dc[i] * j
                    # if 0 <= nr < N and 0 <= nc < N:   # 범위 안에 들어오면, 밖으로 나가는 경우, 인덱스 에러를 막기 위해 경계 설정, 벗 멈추는게 없어서 계속 돔
                    if nr < 0 or nr >= N or nc < 0 or nc >= N:  # 경계 체크 중요
                        break
                    if MAP[nr][nc] == 'H':
                        MAP[nr][nc] = 'X'
    print(f'#{tc}' ,end = ' ')
    ans = 0
    for r in range(N):
        for c in range(N):
            if MAP[r][c] == 'H':
                ans += 1
    print(ans)

        # for line in MAP:
        #     print(line)


