N = int(input())

for i in range(N):
    arr = list(map(int, input().split()))
    arr.sort()
    arr.reverse()
    print(arr[2])