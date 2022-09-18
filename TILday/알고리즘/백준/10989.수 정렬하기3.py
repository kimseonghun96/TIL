N = int(input())
arr = list(input() for _ in range(N))
# print(arr)
arr_list = sorted(arr)

for i in arr_list:
    print(int(i))

