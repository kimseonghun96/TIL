# n = int(input())
# arr = list(map(int, input().split()))
#
# m = int(input())
# arr2 = list(map(int, input().split()))
#
# for i in range(len(arr)):
#     if arr2[i] in arr:
#         print(1)
#     else:
#         print(0)

# 시간초과 발생  ㅜㅜ


# set 자료형은 해시 테이블을 이용하여 구현되어 있으므로, 원소의 존재 여부를 빠르게 확인할 수 있습니다.

n = int(input())
arr = set(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

for x in arr2:
    if x in arr:
        print(1)
    else:
        print(0)