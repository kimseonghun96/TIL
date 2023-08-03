import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

start, end = 1, max(arr)

while start <= end:
    mid = (start + end) // 2
    for i in arr:



