T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    # print(arr)
    answer = []
    for i in range(10):
        answer.append(arr[i])
    # print(answer)
    answer.sort()

    print(f'#{tc} {answer[-1]}')

