icp = {'+': 1, '*': 2, '(': 3, ')': 0}
isp = {'+': 1, '*': 2, '(': 0, ')': 0}

for tc in range(1, 11):
    N = int(input())
    infix = input()
    S = []  # push: List.append(), pop: List.pop()
    postfix = ''
    for token in infix:
        if token in icp:
            if token == ')':
                while S and S[-1] != '(':
                    postfix += S.pop()
                S.pop()
            else:
                while S and icp[token] <= isp[S[-1]]:
                    postfix += S.pop()
                S.append(token)
        else:
            postfix += token
    while S:
        postfix += S.pop()

    # 후위 표기 계산하기
    for token in postfix:
        if token in '+*':
            b = S.pop()
            a = S.pop()
            if token == '+': S.append(a + b)
            else: S.append(a * b)
        else:
            S.append(int(token))

    print(f'#{tc} {S[0]}')