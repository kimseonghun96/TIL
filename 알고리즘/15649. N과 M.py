import sys

input = sys.stdin.readline

n, m = map(int, input().split())

stack = []

def dfs():
    if len(stack) == m:
        print(' '.join(map(str, stack)))
        return

    print('stack', stack)
    for i in range(1, n+1):
        if i in stack:
            continue
        stack.append(i)
        dfs()
        stack.pop()

dfs()