import sys

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    m, n = map(int, input().split())
    items = input().split()
    copy_items = items[:]
    temp = ['check'] * m
    for _ in range(n):
        start, change = map(int, input().split())
        start -= 1
        change -= 1
        temp[change] = items[start]
        copy_items.remove(items[start])

    for i in range(m):
        if temp[i] == 'check':
            temp[i] = copy_items[0]
            copy_items.pop(0)


    print(*temp)

