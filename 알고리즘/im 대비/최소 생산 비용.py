'''
1
3
73 21 21
11 59 40
24 31 83
'''
#DFS를 이용해 모든 경우의 수를 탐색합니다. 각 경우마다 방문한 도시들의 순서를 기억하면서 그 순서에 따라 비용을 계산하고, 그 중 최소 비용을 구한다.

def cost(idx, total):     # 도시의 인덱스, 방문한 도시들의 합
    global result         # 최소 비용을 저장할 result 변수를 전역 변수로 선언

    # 모든 도시를 방문했거나 이미 계산한 결과보다 높은 비용이 나올 경우에는 탐색을 종료
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
    visit = [0 * N for _ in range(N)] # 방문한 도시를 표시하기 위한 visit 리스트
    result = 9999999
    cost(0, 0)

    print(f'#{tc} {result}')

