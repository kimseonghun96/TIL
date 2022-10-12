switch = int(input())  # tmdnlcl
arr1 = list(map(int, input().split()))
arr = [0] * (len(arr1) + 1)
for i in range(len(arr1)):
    if arr1[i] == 1:
        arr[i+1] = 1

N = int(input())
for i in range(N):
    gender, number = map(int, input().split())
    if gender == 1:
        if arr[number] == 1:
            arr[number] = 0

        elif arr[number] == 0:
            arr[number] = 1


    elif gender == 2:
        for k in range(1, len(arr)+1):
            if number-k != number+k:
                if arr[number] == 1:
                    arr[number] = 0
                elif arr[number] == 0:
                    arr[number] = 1
                    break

            else:
                if arr[number-k] == 1:
                    arr[number-k] = 0
                    arr[number+k] = 0


                elif arr[number-k] == 0:
                    arr[number-k] = 1
                    arr[number+k] = 1


ans = []
for i in range(1, len(arr)):
    ans.append(arr[i])

print(ans)

