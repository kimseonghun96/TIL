k, n = map(int, input().split())
lanlist = []
for _ in range(k):
    lanlist.append(int(input()))
left = 1
right = max(lanlist)

while left <= right:
    middle = (left + right) // 2
    ans = 0
    for i in lanlist:
        ans += i // middle

    if ans >= n:
        left = middle + 1
    elif ans < n:
        right = middle - 1

print(right)