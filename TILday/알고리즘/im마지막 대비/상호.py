'''
1
3 7
***....
*-..#**
#<.****
23
SURSSSSUSLSRSSSURRDSRDS
'''
T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    arr = [list(input()) for _ in range(H)]
    N = int(input())                            # 문자열 길이
    str_list = list(input())

    d_list = ['<', '>', 'v', '^']               # 동작
    # 시작점 부터 찾자
    nr, nc = 0, 0
    for i in range(H):
        for j in range(W):
            if arr[i][j] in d_list:     # 시작점 찾았다
                nr = i
                nc = j

    for i in range(N):                  # 입력된 문자에 따라 작동
        if str_list[i] == 'L':
            arr[nr][nc] = '<'          # 왼쪽 이동
            if 0 <= nc - 1 < W and arr[nr][nc-1] == '.':  # 왼쪽으로 한칸 이동하는 것이 범위를 벗어나지 않고, 이동할 수 있는 곳이라면
                nc = nc - 1
                arr[nr][nc] = '<'     # 이동
                arr[nr][nc+1] = '.'       # 전에 있던 곳은 평지로

        elif str_list[i] == 'R':
            arr[nr][nc] = '>'
            if 0 <= nc + 1 < W and arr[nr][nc+1] == '.':
                nc = nc+1
                arr[nr][nc] = '>'     # 이동
                arr[nr][nc-1] = '.'       # 전에 있던 곳은 평지로

        elif str_list[i] == 'U':
            arr[nr][nc] = '^'
            if 0 <= nr - 1 < H and arr[nr-1][nc] == '.':
                nr = nr-1
                arr[nr][nc] = '^'     # 이동
                arr[nr+1][nc] = '.'       # 전에 있던 곳은 평지로

        elif str_list[i] == 'D':
            arr[nr][nc] = 'v'
            if 0 <= nr + 1 < H and arr[nr+1][nc] == '.':
                nr = nr +1
                arr[nr][nc] = 'v'     # 이동
                arr[nr-1][nc] = '.'       # 전에 있던 곳은 평지로

        elif str_list[i] == 'S':
            for t in range(1, 21):  # H,W의 범위 최대 20
                if arr[nr][nc] == '<':
                    sc = nc - t            # 왼쪽으로 쏠 건디
                    if 0 <= sc < W and arr[nr][sc] == '#':     # 강철벽이라면 멈추고
                        break
                    elif 0 <= sc < W and arr[nr][sc] == '*':   # 벽돌로 만들어진 벽이라면
                        arr[nr][sc] = '.'                       # 평지로 만들고 멈춰야됨
                        break


                elif arr[nr][nc] == '>':
                    sc = nc + t
                    if 0 <= sc < W and arr[nr][sc] == '#':     # 강철벽이라면 멈추고
                        break
                    elif 0 <= sc < W and arr[nr][sc] == '*':   # 벽돌로 만들어진 벽이라면
                        arr[nr][sc] = '.'                       # 평지로 만들고 멈춰야됨
                        break


                elif arr[nr][nc] == '^':
                    sr = nr - t
                    if 0 <= sr < H and arr[sr][nc] == '#':     # 강철벽이라면 멈추고
                        break
                    elif 0 <= sr < H and arr[sr][nc] == '*':   # 벽돌로 만들어진 벽이라면
                        arr[sr][nc] = '.'                       # 평지로 만들고 멈춰야됨
                        break

                elif arr[nr][nc] == 'v':
                    sr = nr + t
                    if 0 <= sr < H and arr[sr][nc] == '#':     # 강철벽이라면 멈추고
                        break
                    elif 0 <= sr < H and arr[sr][nc] == '*':
                        arr[sr][nc] = '.'                       # 평지로 만들고 멈춰야됨
                        break


    print(f'#{tc}', end = ' ')
    for i in arr:
        print(''.join(i))


