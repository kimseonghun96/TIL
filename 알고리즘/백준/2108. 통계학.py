import sys
from collections import Counter

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()

print(round(sum(arr) / len(arr)))
print(arr[len(arr)//2])

# 최빈값 - 빈출
cnt_li = Counter(arr).most_common()
if len(cnt_li) > 1 and cnt_li[0][1] == cnt_li[1][1]: #최빈값 2개 이상
    print(cnt_li[1][0])
else:
    print(cnt_li[0][0])


print(max(arr) - min(arr))


# 최빈값 - 빈출
# 파이썬에 Counter함수가 있으나 사용하지않음 !!
# number = list(set(li)) # 중복제거
# max_fre = []
# max_cnt = 0
# for i in number:
#     #print(i, li.count(i))
#     if max_cnt == li.count(i):
#         max_fre.append(i)
#     elif max_cnt < li.count(i):
#         max_fre = []
#         max_fre.append(i)
#         max_cnt = li.count(i)
# if len(max_fre) > 1: # 최빈값이 2개이상
#     max_fre.sort()
#     print(max_fre[1])
# else: # 최빈값 1개
#     print(max_fre[0])