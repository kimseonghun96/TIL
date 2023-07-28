import sys
input = sys.stdin.readline

T = int(input())

def binary_search(target, arr):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return 1  # 찾았으면 1을 반환
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return 0  # 찾지 못했으면 0을 반환


for tc in range(T):
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    M = int(input())
    arr2 = list(map(int, input().split()))

    for i in arr2:
        print(binary_search(i, arr))

