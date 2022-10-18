T = int(input())

for tc in range(1, T+1):

    arr = [input() for _ in range(5)] # 5개의 텍스트 리스트 저장

    max_len = 0     # 가장 길이가 긴 것을 다을 것, 짧은 것을 긴 것의 길이 만큼 만들어 주기 위해.
                    # 가장 긴 것이 5가 아닐 수도 있다.

    # 하나 씩 길이를 재야됨 가로
    for text in arr:                # max_len에 가장 길이가 긴 리스트를 저장
        if max_len < len(text):
            max_len = len(text)

    # max_len보다 짧은 list들을 ' '으로 채워 줌
    for i in range(5):
        if len(arr[i]) < max_len:     #arr[i]의 길이가 max_l보다 작다면
            arr[i] += ' '*(max_len - len(arr[i]))   # arr[i]에 빈 칸을 추가 해줌 max_len과 차이나는 수 만큼

    #세로로 읽을 정답 저장
    answer = ''

    #리스트를 세로로 읽으면서, ' '를 제외한 나머지를 저장
    for r in range(max_len):
        for c in range(5):
            if arr[c][r] != ' ':
                answer += arr[c][r]

    print(f'#{tc} {answer}')


