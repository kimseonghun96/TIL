# 버섯 리스트를 만들고
# 하나씩 더해가면서 더한값이 100을 넘었을 때
# 100에서 그 전값 뺀거랑 더한값에 100을 뺀거랑 비교해서
# 출력하면 될 듯

arr = []
for i in range(10):
    arr.append(int(input()))

sum_arr = 0

for i in range(len(arr)):
    sum_arr += arr[i]
    if sum(arr) < 100:
        print(sum(arr))
        break
    if sum_arr == 100:
        print(sum_arr)
        break
    elif sum_arr > 100:
        if 100 - sum(arr[:i]) >= sum_arr - 100:
            print(sum_arr)
            break

        elif 100 - sum(arr[:i]) < sum_arr - 100:
            print(sum(arr[:i]))
            break





