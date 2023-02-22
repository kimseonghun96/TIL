n = 10

arr = [2, 3]
result = 0
ans = 0

while True:
    for num in arr:
        result += n % num
        ans += 1
    if result == 0:
        break

print(ans)
