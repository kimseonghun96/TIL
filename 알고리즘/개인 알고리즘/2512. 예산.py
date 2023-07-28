import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

def check_sum(mid):
    total = 0
    for i in arr:
        if i <= mid:
            total += i
        else:
            total += mid
    return total

if sum(arr) <= M:
    print(max(arr))
else:
    start, end = 0, max(arr)
    while start <= end:
        mid = (start + end) // 2
        if check_sum(mid) <= M:
            start = mid + 1
        else:
            end = mid - 1

    print(end)
