import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

def binary_search(M, arr):
    start, end = 0, max(arr)
    while start <= end:
        mid = (start + end) // 2
        ans = 0
        for i in arr:
            if i > mid:
                ans += i - mid
        if ans >= M:
            start = mid + 1
        else:
            end = mid - 1
    return end

print(binary_search(M, arr))
