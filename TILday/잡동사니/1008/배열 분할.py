'''
3
5
2 6 8 5 -8
5
-2 -2 -5 -8 5
6
1 -5 7 -6 8 3
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    ans = []
    # 2 분할
    for i in range(1, N-1):
        for j in range(i+1, N):
            temp = [sum(arr[0:i]), sum(arr[i:j]), sum(arr[j:N])]
            ans.append(max(temp) - min(temp))

    print(f'#{tc}', min(ans))
