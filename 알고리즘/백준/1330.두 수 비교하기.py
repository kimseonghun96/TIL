# 간단하게 크기 비교
A, B = map(int, input().split())
if A > B:
    print('>')
if A == B:
    print('==')
if A < B:
    print('<')