'''
2
ABCDE
abcde
01234
FGHIJ
fghij
AABCDD
afzz
09121
a8EWg6
P5h3kx
'''


T = int(input())
for tc in range(1, T+1):
    arr = [list(map(str, input())) for _ in range(5)]
    # print(arr)

    # 문자열의 최대 길이 구하기
    # for문의 범위 정하기 위해
    max_len = 0

    # 매번 길이를 확인할 수 없기 때문에 length에 문자열의 길이를 저장
    length = []

    for i in arr:
        length.append(len(i))
        if len(i) > max_len:
            max_len = len(i)
    # print(length)
    print(max_len)

    answer = ''
    for i in range(max_len):
        for j in range(5):
            if length[j] > i:
                answer += arr[j][i]

    print(f'#{tc} {answer}')

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

    #리스트를 세로로 읽으면서, ' '를 제외한 나머지를 저장한다.
    for r in range(max_len):
        for c in range(5):
            if arr[c][r] != ' ':
                answer += arr[c][r]
    # print(answer)
    print(f'#{tc} {answer}')