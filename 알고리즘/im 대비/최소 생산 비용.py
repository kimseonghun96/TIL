'''
1
3
73 21 21
11 59 40
24 31 83
'''


def cost(idx, total):
    global result
    if total >= result:
        return
    if idx == N:
        result = total
        return

    for i in range(N):
        if not visit[i]:
            visit[i] = 1
            cost(idx+1, total + arr[idx][i])
            visit[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [0 * N for _ in range(N)]
    result = 9999999
    cost(0, 0)

    print(f'#{tc} {result}')

