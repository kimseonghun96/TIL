T = int(input())
for tc in range(1, T+1):
    result = list(input())

    answer = 0
    cnt = 0
    for i in result:
        if i =='O':
            cnt += 1
            answer += cnt
        else:
            cnt = 0

    print(answer)