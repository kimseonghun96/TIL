# 문제에 따라 작성

import sys

input = sys.stdin.readline

stack = []

N = int(input())

for i in range(N):
    arr = input().split()
    order = arr[0]

    if order == 'push':
        stack.append(arr[1])

    elif order == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif order == 'size':
        print(len(stack))

    elif order == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif order == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

