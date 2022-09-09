

for T in range(10):
    tc = int(input())
    # print(f'#{tc}')
    arr = [list(map(str, input())) for _ in range(100)]
    # print(f'#{tc} {arr}')

    zip_arr = list(zip(*arr))

    answer = 0
    for i in range(100):
        for j in range(100):
            for k in range(100):
                if arr[i][j:j+k+1] == arr[i][j:j+k+1][::-1]: #가로 회문 찾고
                    if answer < len(arr[i][j:j+k+1]):
                        answer = len(arr[i][j:j+k+1])


                if zip_arr[i][j:j+k+1] == zip_arr[i][j:j+k+1][::-1]:
                    if answer < len(zip_arr[i][j:j+k+1]):        # 세로 회문 찾았다
                        answer = len(zip_arr[i][j:j+k+1])

    print(f'#{tc} {answer}')