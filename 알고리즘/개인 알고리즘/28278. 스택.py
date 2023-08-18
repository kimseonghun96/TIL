# 1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
# 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
# 3: 스택에 들어있는 정수의 개수를 출력한다.
# 4: 스택이 비어있으면 1, 아니면 0을 출력한다.
# 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다

import sys

input = sys.stdin.readline

T = int(input())
arr = []
for tc in range(T):
    step = list(map(int, input().split()))
    num = step[0]
    X = 0
    if len(step) == 2:
        X = step[1]
    if num == 1:
        arr.append(X)
    elif num == 2:
        if len(arr) >= 1:
            print(arr[-1])
            arr.pop()
        else:
            print(-1)

    elif num == 3:
        print(len(arr))

    elif num == 4:
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(arr) >= 1:
            print(arr[-1])
        else:
            print(-1)
