T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())  # H = 높이, W = 너비
    arr = [list(input()) for _ in range(H)]
    N = int(input())
    str_lst = list(input())                          # SURSSSSUSLSRSSSURRDSRDS
    w_lst = ['<', '>', 'v', '^']

    nr, nc = 0, 0
    for r in range(H):                               # 완전 탐색을 하면서
        for c in range(W):
            for k in w_lst:                          # w_list 안에 있으면
                if arr[r][c] == k:
                    nr = r                           # nr, nc로 저장
                    nc = c

    for i in range(N):
        if str_lst[i] == 'U':
            arr[nr][nc] = '^'
            if 0 <= nr - 1 < H and arr[nr - 1][nc] == '.':      # 범위 설정 앞이 이동가능한 곳이면
                nr = nr - 1                                     # 위치 이동
                arr[nr][nc] = '^'                               # 방향 설정
                arr[nr + 1][nc] = '.'                           # 전에 있던 장소 .
        elif str_lst[i] == 'R':
            arr[nr][nc] = '>'
            if 0 <= nc + 1 < W and arr[nr][nc + 1] == '.':
                nc = nc + 1
                arr[nr][nc] = '>'
                arr[nr][nc - 1] = '.'
        elif str_lst[i] == 'L':
            arr[nr][nc] = '<'
            if 0 <= nc - 1 < W and arr[nr][nc - 1] == '.':
                nc = nc - 1
                arr[nr][nc] = '<'
                arr[nr][nc + 1] = '.'
        elif str_lst[i] == 'D':
            arr[nr][nc] = 'v'
            if 0 <= nr + 1 < H and arr[nr + 1][nc] == '.':
                nr = nr + 1
                arr[nr][nc] = 'v'
                arr[nr - 1][nc] = '.'
        elif str_lst[i] == 'S':                                             # 포격하는겨
            for num in range(1, 20 + 1):
                if arr[nr][nc] == '<':                                      # 각케이스마다 포격
                    if 0 <= nc - num < W and arr[nr][nc - num] == '#':
                        break
                    elif 0 <= nc - num < W and arr[nr][nc - num] == '*':
                        arr[nr][nc - num] = '.'
                        break
                elif arr[nr][nc] == '>':
                    if 0 <= nc + num < W and arr[nr][nc + num] == '#':
                        break
                    elif 0 <= nc + num < W and arr[nr][nc + num] == '*':
                        arr[nr][nc + num] = '.'
                        break
                elif arr[nr][nc] == 'v':
                    if 0 <= nr + num < H and arr[nr + num][nc] == '#':
                        break
                    elif 0 <= nr + num < H and arr[nr + num][nc] == '*':
                        arr[nr + num][nc] = '.'
                        break
                elif arr[nr][nc] == '^':
                    if 0 <= nr - num < H and arr[nr - num][nc] == '#':
                        break
                    elif 0 <= nr - num < H and arr[nr - num][nc] == '*':
                        arr[nr - num][nc] = '.'

    print(f'#{tc}', end=' ')
    for line in arr:
        print(''.join(line))
