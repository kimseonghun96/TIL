# 2차원 배열 행 열 한줄 씩 담아서
# X 가 그 줄에 없으면 ans +1 zip_ans + 1


N, M = map(int, input().split())

castle = [list(input()) for _ in range(N)]

ans = 0
zip_ans = 0

for i in range(N):
    has_guard = False
    for j in range(M):
        if castle[i][j] == 'X':
            has_guard = True
            break
    if not has_guard:
        ans += 1

for j in range(M):
    has_guard = False
    for i in range(N):
        if castle[i][j] == 'X':
            has_guard = True
            break
    if not has_guard:
        zip_ans += 1

print(max(ans, zip_ans))



