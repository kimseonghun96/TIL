n = int(input())

arr1 =[]
arr0 = []

for i in range(n):
    check = int(input())
    if check == 1:
        arr1.append(i)
    else:
        arr0.append(i)

if len(arr1) > len(arr0):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")