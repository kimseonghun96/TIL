# 이진탐색을 이용해서 풀자

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    start = 0
    end = N//2
    ans = -1
    while start <= end:
        middle = (start+end)//2
        if middle**3 > N:
            end = middle -1
        elif middle**3 < N:
            start = middle + 1
        elif middle**3 == N:
            ans = middle
            break

        if N == 1:
            ans = 1
            break

    print(f'#{tc} {ans}')
