'''
1
10, 10
1 2 3 4 5 6 7 8 9 10
'''
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    arr = []
    for i in range(1, 13):
        arr.append(i)
    # print(arr)
    sum_box = []
    for i in range(1<<len(arr)):
        box =[]
        for j in range(len(arr)):
            if i & (1<<j):
                box.append(arr[j])
        if len(box) == N:
            sum_box.append(sum(box))

    print(f'#{tc}', sum_box.count(K))

