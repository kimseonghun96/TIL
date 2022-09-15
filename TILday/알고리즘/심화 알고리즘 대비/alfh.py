move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def boundary(y, x): # 경계 체크
    if y < 0 or x < 0 or y >= n or x >= n:
        return True  # 경계 벗어남
    return False

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    map_list = [list(map(int, list(input()))) for _ in range(n)]
    y, x = 0, 0  # 시작좌표
    result = 0  # 통로 연결되면 1로 바뀜
    # 출발점(2) 찾기
    for i in range(n):
        if 2 in map_list[i]:
            x = map_list[i].index(2)
            y = i
            break
    stack = [(y, x)]  # 스택에 시작좌표 넣기
    # 스택이 빌때까지 반복
    while stack:
        y, x = stack.pop()  # 현재 좌표 꺼내서
        map_list[y][x] = 1  # 현재 좌표 방문처리
        # 이동할 4방향 검사
        for _y, _x in move:
            dy = y + _y
            dx = x + _x
            # 경계 벗어나면 다음 길로
            if boundary(dy, dx):
                continue
            if map_list[dy][dx] == 3:  # 도착하면
                result = 1
                break  # 결과 바꾸고 반복문 종료
            # 통로(0)를 만나면 스택에 추가
            elif not map_list[dy][dx]:
                stack.append((dy, dx))
        else:  # 브레이크 없이 끝나면 다음으로 진행
            continue
        break
    print(f'#{tc} {result}')