import sys

input = sys.stdin.readline

N = int(input())

def binary_search(N):
    start, end = 0, 2 ** 63
    while start <= end:
        mid = (start + end) // 2
        if mid ** 2 == N:
            return mid
        elif mid ** 2 < N:
            start = mid + 1
        else:
            end = mid - 1
    return start

print(binary_search(N))

