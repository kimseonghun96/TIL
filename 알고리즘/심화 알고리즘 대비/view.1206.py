# 건물 한개를 정하고 뒤의 두개 와 같지 않고 앞뒤 두개 보다 크다면
# 앞 뒤 두개의 건물 중 가장 큰 것과
# 건물을 빼주고 그 값을 더해 나간다.

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    # print(arr)
    ans = 0
    for i in range(2, N-2):
        if arr[i] > 0:
            if arr[i] == arr[i+1] and arr[i] == arr[i+2]:
                pass

            elif arr[i] > arr[i+1] and arr[i] > arr[i+2] and arr[i] > arr[i-1] and arr[i] > arr[i-2]:
                arr2 = [arr[i-1], arr[i+1], arr[i-2], arr[i+2]]
                arr2.sort()
                ans += arr[i] - arr2[-1]
    print(ans)