n, k = map(int, input().split())
arr = list(map(int, input().split(',')))


for i in range(k):
    temp = []
    # 이렇게 하면 마지막 값은 순회하지 않으므로 빠짐 없이 모든 값의 차이를 계산할 수 있다.
    for j in range(1, len(arr)):
        temp.append(arr[j]-arr[j-1])
    arr = temp

print(*arr, sep= ",")

