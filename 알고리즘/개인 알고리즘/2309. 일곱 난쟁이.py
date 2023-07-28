# 총 9명의 난쟁이 중
# 합이 100이 되는 7명을 구해야되는데
# 기존의 9명의 키의 합에서 100을 빼고
# 나온 값을 리스트에서 두개가 맞으면
# 그거 값만 빼고 추출하면 되잖아

n = 9
nan_list = []

for i in range(n):
    nan_list.append(int(input()))

nan_list = sorted(nan_list)

sum_nan = sum(nan_list)

subtract = sum_nan - 100

for i in range(n-1):
    for j in range(i+1, n):
        if nan_list[i] + nan_list[j] == subtract:
            del nan_list[j]
            del nan_list[i]
            break
    if len(nan_list) == 7:
        break

for i in range(7):
    print(nan_list[i])