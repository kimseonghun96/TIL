Y = 30
M = 60
N = int(input())
Call = list(map(int, input().split()))

Y_ans = 0
M_ans = 0

for i in range(N):
    Y_ans += Call[i] // Y + 1
    M_ans += Call[i] // M + 1

y = 10 * Y_ans
m = 15 * M_ans


if m > y:
    print('Y', y)
elif m < y:
    print('M', m)
else:
    print('Y', 'M', m)



