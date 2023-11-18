import sys

input = sys.stdin.readline

n, k = map(int, input().split())

arr = list(map(int, input().split()))

temp = []

for i in arr:
    if i not in temp:
        temp.append(i)
    else:
        if temp.count(i) == k:
            pass
        else:
            temp.append(i)

ans = [temp[0]]

def longest_length(ans):
    consecutive_length = 1
    max_consecutive_length = 1

    for i in range(1, len(ans)):
        if ans[i] - ans[i - 1] == 1 or - 1:
            consecutive_length += 1
        else:
            max_consecutive_length = max(max_consecutive_length, consecutive_length)
            consecutive_length = 1

        # 중복된 숫자가 연속되면 중단
        if ans[i] == ans[i - 1]:
            consecutive_length = 1

    return max(max_consecutive_length)


print(longest_length(temp))