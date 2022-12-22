T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(input()))

    zip_arr = list(zip(*arr))

    answer = 0

    for i in range(N):
        for j in range(N-M+1):
            if arr[i][j:j+M] == arr[i][j:j+M][::-1]:
                answer = arr[i][j:j+M]
            if zip_arr[i][j:j+M] == zip_arr[i][j:j+M][::-1]:
                answer = zip_arr[i][j:j+M]
    answer = ''.join(answer)
    print(f'#{tc} {answer}')