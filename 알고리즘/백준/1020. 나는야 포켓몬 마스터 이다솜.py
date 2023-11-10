## 다시풀기

import sys

input = sys.stdin.readline
n, m = map(int, input().split())

poket = dict()
poket_num = dict()

for i in range(1, n+1):
    poketmon = input().strip()
    poket[poketmon] = i
    poket_num[i] = poketmon

for i in range(m):
    question = input().strip()
    if question.isdigit():
        print(poket_num[int(question)])
    else:
        print(poket[question])
