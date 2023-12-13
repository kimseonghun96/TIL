n = int(input())
arr = list(map(int, input().split()))

ans = []

while 0 < len(arr):
    ans.append(min(arr) + max(arr))
    arr.remove(min(arr))
    arr.remove(max(arr))

print(min(ans))