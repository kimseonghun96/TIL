'''
3
10 50
4 22 1 12 11 36 21 23 3 36
11 50
4 22 1 12 11 6 21 23 3 36 6
10 50
3 2 5 5 1 13 23 17 50 25
'''
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    jewelry = list(map(int, input().split()))

    box = [4, 6, 7, 9, 11]

    all_box = []
    for i in range(len(box)):
        for j in range(1, 30):
            if box[i] * j <= 100:
                all_box.append(box[i]*j)
    # print(all_box)

    buy_box = []
    for i in range(len(jewelry)):
        if jewelry[i] in all_box:
            buy_box.append(jewelry[i])
    # print(buy_box)

    sum_box = []
    for i in range(1 << len(buy_box)):
        temp = []
        for j in range(len(buy_box)):
            if i & (1 << j):
                temp.append(buy_box[j])
        sum_box.append(sum(temp))
    # print(sum_box)

    ans = []
    for i in range(len(sum_box)):
        if sum_box[i] <= 50:
            ans.append(sum_box[i])

    print(f'#{tc}', max(ans))