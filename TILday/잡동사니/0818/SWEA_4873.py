T = int(input())
for tc in range(1, T+1):
    str = input()
    top = 0
    stack = []

    for i in range(len(str)):
        if len(stack) == 0:         # stack 에 아무것도 없을 때
            stack.append(str[i])    # 첫[i] 생김

        else:
            stack.append(str[i])    # stack 생겼으니까 나머지 하나씩 추가 추가
            top += 1                # top 올림

            # stack이랑 top 준비됐음

            if stack[top] == stack[top-1]:
                stack.pop()         # 똑같은 두 개 날림
                stack.pop()
                top -= 2            # 두 개 날렸으니까 top에서도 빼줌
                if top < 0:         # 시작부터 2개 날리면 -로 가기 때문에
                    top = 0         # - 안가게 제약 걸어줌

    len_stack = len(stack)
    print(f'#{tc} {len_stack}')


