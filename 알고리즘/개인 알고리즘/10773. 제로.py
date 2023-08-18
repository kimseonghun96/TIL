arr = []

K = int(input())

for _ in range(K):
    check = int(input())
    if check != 0:
        arr.append(check)
    else:
        arr.pop()

print(sum(arr))