T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    # print(arr)
    answer = 0
    for i in range(10):
        if arr[i] % 2 == 0:
            pass
        else:
            answer += arr[i]

    print(f'#{tc} {answer}')
