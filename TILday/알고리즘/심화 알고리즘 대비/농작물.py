'''
1
5
14054
44250
02032
51204
52212
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans = 0
    for i in range(N):
        arr = list(map(int, input()))
        if i == 0:
            ans += arr[N//2]
    # print(ans)
        elif 0 < i < N//2:
            for j in range(N//2-i, N//2+i+1):
                ans += arr[j]
    # print(ans) 11
        elif i == N//2:
            ans += sum(arr)
    # print(ans) 18
        elif N//2 < i < N:
            for j in range(i-N//2, N-(i-N//2)):
                # if 0 < j < N:
                ans += arr[j]
    #
    # print(ans)

        elif i == N:
            ans += arr[N//2]


    print(f'#{tc} {ans}')
