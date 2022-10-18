T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    temp = []
    for i in range(1, N+1):
        temp.append(i)

    if temp == arr:
        print(f'#{tc}', 'Yes')
    else:
        print(f'#{tc}', 'No')
    # for i in range(len(arr)):
    #     if arr[i] == temp[i]:
    #         print(f'#{tc}', 'Yes')
    #     else:
    #         print(f'#{tc}', 'No')
