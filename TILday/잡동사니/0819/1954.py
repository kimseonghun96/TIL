#  이곳에 코드와 주석을 작성합니다.
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]

    r, c = (0, -1)  # 기본적으로 맵 바깥의 우상단 좌측에서 시작한다고 생각.
    dr = [0, 1, 0, -1]  # 우 -> 하 -> 좌 -> 상이 한 사이클이라고 생각
    dc = [1, 0, -1, 0]

    num = 1  # 1부터니까
    turn = 0  # 일단 오른쪽부터 진행
    for i in range(N * 2, 1, -1):  # 4 by 4면 4 3 3 2 2 1 1 이 돼야 하니까!
        for j in range(i // 2):
            r += dr[turn % 4]
            c += dc[turn % 4]
            snail[r][c] = num  # 숫자를 집어넣고
            num += 1  # 다음 크기의 숫자로 증액

        turn += 1  # 한 방향이 돌고나면 방향 turn!

    print('#{}'.format(tc))
    for _ in range(N):
        print(*snail[_])