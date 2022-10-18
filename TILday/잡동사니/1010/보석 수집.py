'''
3
10 50
4 22 1 12 11 36 21 23 3 36
11 50
4 22 1 12 11 6 21 23 3 36 6
10 50
3 2 5 5 1 13 23 17 50 25
'''
# 내가 고를 수 있는 모든 보석의 수를 리스트로 만든다.
# 입력 받은 보석의 수 중에 모든 보석의 수에 해당하는 것만
# 따로 뽑아 리스트를 만들고
# 그 리스트의 부분 집합의 합 중 50 이하인 것 만 뽑아
# 그 중 가장 큰 것을 출력한다.

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    buy_list = [4, 6, 7, 9, 11]

    # 살 수 있는 숫자의 배수중 100이하의 것을 모두 뽑는다.
    all_box = []
    for i in range(len(buy_list)):
        for j in range(1, 26):
            if buy_list[i]*j <= 100:
                all_box.append(buy_list[i] * j)

    # 입력 받은 arr이 all_box에 해당되는 것만 따로 뽑음
    rusult = []
    for i in range(len(arr)):
        if arr[i] in all_box:
            rusult.append(arr[i])

    # result의 부분집합을 모두 구해서 50 이하인 것만 따로 뽑음
    ans = []
    for i in range(1<<len(rusult)):
        temp = []
        for j in range(len(rusult)):
            if i & (1<<j):
                temp.append(rusult[j])
        if sum(temp) <= 50:
            ans.append(sum(temp))

    # ans 중 가장 큰 값을 뽑는다.
    print(f'#{tc}', max(ans))
