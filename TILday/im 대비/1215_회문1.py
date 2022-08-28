import sys
sys.stdin = open('test_input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(8)]
    # print(arr)
    zip_arr = list(zip(*arr))
    # print(zip_arr)

    answer = 0
    for r in range(8):
        for c in range(8 - N +1):
            if arr[r][c:c+N] == arr[r][c:c+N][::-1]:
                answer +=1

    for r in range(8):
        for c in range(8 - N + 1):
            if zip_arr[r][c:c+N] == zip_arr[r][c:c+N][::-1]:
                answer +=1


    print(f'#{tc} {answer}')