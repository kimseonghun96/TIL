N = int(input())

arr = list(map(int, input().split()))
arr.sort()

ans = []

for i in range(N):
    ans.append(sum(arr[0:i])+arr[i])

print(sum(ans))
