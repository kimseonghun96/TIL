# 각 랜선을 나누는 수 중에
# 목이 N을 넘는 값을 구해야 함

K, N = map(int, input().split())

line = []

for i in range(K):
    line.append(int(input()))

start = 1           # N은 1이상
end = max(line)

while start <= end:
    mid = (start + end) // 2
    ans = 0
    for i in line:
        ans += i // mid
    # N개보다 많이 만드는 것도 N개를 만드는 것에 포함
    if ans >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)


