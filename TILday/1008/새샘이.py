'''
2
1 2 3 4 5 6 7
5 24 99 76 1 77 6
'''

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    ans_sum = set()
    for i in range(len(arr)):
        for j in range(len(arr)):
            for k in range(len(arr)):
                if arr[i] != arr[j] and arr[i] != arr[k] and arr[j] != arr[k]:
                    ans_sum.add(arr[i]+arr[j]+arr[k])

    # print(ans_sum)
    ans_sum = list(ans_sum)
    ans_sum.sort()
    ans_sum = ans_sum[::-1]
    print(f'#{tc}', ans_sum[4])