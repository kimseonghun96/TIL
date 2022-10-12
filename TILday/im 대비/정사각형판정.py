'''
1
4
#..#
....
....
#..#
'''
dr = [0, 1]
dc = [1, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    ans = 'yes'

    side = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '#':
                side.append((i, j))
                break

    side2 = side[0]   # '#'의 첫번 째 좌표

    r_side = 0  # 변의 길이
    c_side = 0
    for k in range(2):
        r_temp = 0
        c_temp = 0
        for t in range(N):
            r = side2[0]
            c = side2[1]
            nr = r + dr[k] * t
            nc = c + dc[k] * t

            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][c] == '.' or arr[r][nc] == '.':
                    break

                elif 0 <= nr < N and 0 <= nc < N:
                    if arr[nr][c] == '#':
                        r_temp += 1
                    if arr[r][nc] == '#':
                        c_temp += 1

        r_side = r_temp
        c_side = c_temp

    cnt = 0                 # 총 #의 개수
    for x in range(N):
        for y in range(N):
            if arr[x][y] == '#':
                cnt += 1
    if cnt != (r_side)**2:    # 정사각형의 개수와 총 #의 개수가 다르면 no
        ans = 'no'


    box = 0                     # 범위 안의 # 개수 파악
    if r_side != c_side:        # 두 변의 길이가 다르면 또 no
        ans = 'no'
    else:                       # 같을경우
        for i in range(r, r+ r_side):
            for j in range(c, c + c_side):
                if 0 <= i < N and 0 <= j < N:
                    if arr[i][j] == '#':
                        box += 1

    if box == cnt or cnt == 1 or cnt == N*N:
        pass
    else:
        ans = 'no'


    print(f'#{tc} {ans}')
    print(box)




