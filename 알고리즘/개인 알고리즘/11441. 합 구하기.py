import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

sum_arr = [arr[0]]

for t in range(1, N):
    sum_arr.append(arr[t]+sum_arr[t-1])

# print(sum_arr)

for k in range(M):
    i, j = map(int, sys.stdin.readline().split())
    if i == j:
        print(arr[i-1])
    elif i == 1:
        print(sum_arr[j-1])
    else:
        print(sum_arr[j - 1] - sum_arr[i - 2])
