n = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = 0


for i in range(len(arr)):
    ans += sum(arr[0:i+1])

print(ans)