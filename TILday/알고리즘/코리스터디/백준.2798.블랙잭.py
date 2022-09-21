N, M = map(int, input().split())
arr = list(map(int, input().split()))

ans = []
# 포문 순열 N개의 카드 중 3개 씩 뽑음
# 블랙잭 특성상 중복 카드 없음
# M과 같거나 작은 수를 리스트에 담고
# 리스트에서 가장 큰 수를 답으로 출력
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i != j and j !=k and i !=k:
                if arr[i] + arr[j] + arr[k] <= M:
                    # print(arr[i],arr[j] ,arr[k])
                    ans.append(arr[i] + arr[j] + arr[k])

print(max(ans))