T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = []  # 최종 담을 상자 상자 만듬

    for i in range(N):
        temp = []  # 임시 상자
        for j in range(0, i + 1):
            if j == 0 or i == j:  # 대각과 j가 0인 곳을
                temp.append(1)  # 1로 채움

            else:
                temp.append(arr[i - 1][j - 1] + arr[i - 1][j])  # 왼쪽 대각 위, 오른쪽 대각 위의 합을 저장
        arr.append(temp)  # 최종적으로 합침

    print(f'#{tc}')

    for line in arr:
        print(*line)