'''
2
1 2 3 4 5 6 7
5 24 99 76 1 77 6
'''
T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    ans = set()
    ans_arr = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            for k in range(len(arr)):
                if i != j and i != k and j != k:
                    ans.add(arr[i] + arr[j] + arr[k])
                    # print(arr[i], arr[j], arr[k])

    ans = list(ans)
    ans.sort()
    ans_list = ans[::-1]
    print(ans_list)
    print(f'#{tc} {ans_list[4]}')