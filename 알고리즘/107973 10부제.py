n = int(input())
arr = list(map(int, input().split()))

ans = 0

if n == 0:
    print(arr.count(0))
else:
    for i in arr:
        if i % n == 0 and i // n == 1:
            ans += 1


    print(ans)