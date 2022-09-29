'''
반례 모음
[테케]. All in one
5
0

1
0
5
1 1 1 1 1
7
0 5 1 3 4 2 0
20
4 5 2 2 4 3 2 3 3 4 5 7 5 3 5 3 1 3 3 3

[답]. All in one 답
#1 0
#2 0
#3 1
#4 2
#5 5
'''


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0] + list(map(int, input().split())) + [0]
    # print(arr)
    ans = 0
    flag = True
    for i in range(N+1):
        if arr[i] < arr[i+1]:
            flag = True
        elif arr[i] > arr[i+1]:
            if flag:
                ans += 1
                flag = False

    print(f'#{tc} {ans}')
