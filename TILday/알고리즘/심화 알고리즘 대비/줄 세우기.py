'''
5
0 1 1 3 2
'''
N = int(input())
num = list(map(int, input().split()))
ans = []
for i in range(N):
    ans.insert(num[i], i+1)
print(*ans[::-1])