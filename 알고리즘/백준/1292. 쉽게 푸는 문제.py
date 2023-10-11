# 쉽긴해


arr = []

for i in range(1, 46):
    for j in range(i):
        arr.append(i)

# print(len(arr)) #1035개
# print(arr)

a, b = map(int, input().split())
print(sum(arr[a-1:b]))
