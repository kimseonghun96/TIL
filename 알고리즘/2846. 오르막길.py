# 인덱스의 값을 비교해서 전의 인덱스의 값보다 다음 인덱스의 값이 크면
# 그 값을 cnt에 계속 더해 나가고
# 다음 인덱스가 더 작으면 cnt 초기화

N = int(input())

arr = list(map(int, input().split()))

arr.append(0)
ans = []
cnt = 0
for i in range(N):
    if arr[i] < arr[i+1]:
        cnt += arr[i+1] - arr[i]
        ans.append(cnt)
    else:
        cnt = 0

print(max(ans))
