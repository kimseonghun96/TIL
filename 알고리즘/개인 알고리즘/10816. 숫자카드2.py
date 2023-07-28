from collections import Counter

import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

M = int(input())
check_arr = list(map(int, input().split()))

cnt = Counter(arr)
ans = []

# print(cnt)  #Counter({10: 3, 3: 2, -10: 2, 6: 1, 2: 1, 7: 1})

for i in check_arr:
    ans.append(cnt[i])


print(*ans)