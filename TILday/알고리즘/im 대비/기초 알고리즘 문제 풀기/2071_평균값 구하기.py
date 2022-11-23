T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    # print(arr)
    answer = 0
    for i in range(10):
        answer += arr[i]

    answer = round(answer/10)
    print(f'#{tc} {answer}')