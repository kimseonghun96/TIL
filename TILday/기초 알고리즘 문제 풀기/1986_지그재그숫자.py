T = int(input())
for tc in range(1, T+1):
    N = int(input())

    sum = 0
    for i in range(1, N+1) :
        if i%2 == 0 :
            sum -= i
        else :
            sum += i

    print(f'#{tc} {sum}')
