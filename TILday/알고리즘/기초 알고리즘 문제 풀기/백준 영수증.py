'''
260000
4
20000 5
30000 2
10000 6
5000 8
'''
N = int(input())
T = int(input())


a = 0
for i in range(1, T+1):
    receipt, num = map(int, input().split())
    a += receipt * num


if N == a:
    print('Yes')
else:
    print('No')


'''N = int(input())
T = int(input())

a = 0
for i in range(T):
    receipt, num = map(int, input().split())
    a +=receipt * num

if N == a:
    print('Yes')
else:
    print('No')'''