'''
2
1 2 3 4 5 6 7
5 24 99 76 1 77 6
'''
T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    ans = set()
    for i in range(len(arr)-2):
        for j in range(i+1, len(arr)-1):
            for k in range(j+1, len(arr)):
                temp = arr[i] + arr[j] + arr[k]
                ans.add(temp)

    ans = list(ans)
    ans.sort()
    ans = ans[::-1]
    print(ans[4])

