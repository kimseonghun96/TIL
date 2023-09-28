# 오름차 순 하는 겨
# 인덱스는 0부터

N, K = map(int, input().split())

arr = list(map(int,input().split()))

arr = sorted(arr)


print(arr[K-1])