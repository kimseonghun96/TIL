T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]
    answer = 99999999999999999
    check = [0]*N

    def perm(depth, acc):
        global answer

        if acc >= answer:  # 백트래킹
            return  # 이미 해당 뎁스에서 구해진 최솟값보다 크거나 같으면 의미 x

        if depth == N:  # 최후 뎁스 도달 시,
            if answer > acc:
                answer = acc  # 최솟값 갱신 시도
            return  # 아니라도 일단 리턴

        for i in range(N):  # 각 층에서 N개의 화살표를 던짐.
            if not check[i]:
                check[i] = 1
                perm(depth + 1, acc + nums[depth][i])  # 이 층까지의 합산액에 더해서 다음 층!
                check[i] = 0

    perm(0, 0)

    print('#{} {}'.format(tc, answer))