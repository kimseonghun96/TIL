N = 99999

while N:
    num = input()
    if num == '0':
        break

    num_list = list(map(int, num))
    # print(type(a.split()))
    # print(b)
    cnt = 2
    cnt += len(num_list) - 1
    for i in num_list:
        if i == 1:
            cnt += 2
        elif i == 0:
            cnt += 4
        else:
            cnt += 3
    print(cnt)

