'''
4
5
2 6 8 5 -8
5
-2 -2 -5 -8 5
6
1 -5 7 -6 8 3
'''
# 조합 연습

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    ans = 9999999999999

    for i in range(1, N-1): # 1, 4
        # print(temp)
        for j in range(i+1, N ): #2, 5
            temp = []
            # print(arr[0:i], arr[i:j], arr[j:N])
            temp.append(sum(arr[0:i]))
            temp.append(sum(arr[i:j]))
            temp.append(sum(arr[j:N]))
            # print(temp)
            temp.sort()
            # print(temp)
            if ans > temp[-1]-temp[0]:
                ans = temp[-1]-temp[0]
            # ans.append(temp[-1]-temp[0])
    #     # print(temp)
    print(f'#{tc} {ans}')

