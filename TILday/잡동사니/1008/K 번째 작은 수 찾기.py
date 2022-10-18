'''
3
7 5
1 3 5 6 4 4 6
10 5
1 3 4 2 3 7 1 6 9 2
10 5
4 7 5 5 1 5 4 4 3 3
'''
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    ans = [0] * (N+1)
    sort_arr = sorted(arr)
    sort_arr = sort_arr + [0]
    # print(arr)
    for i in range(N+1):
        if i < N:
            if sort_arr[i] != sort_arr[i+1]:
                ans[i] = sort_arr[i]
    # print(ans)
    ans = set(ans)
    # print(ans)
    ans = list(ans)
    print(f'#{tc} {ans[M]}')
