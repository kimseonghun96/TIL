n, l = map(int, input().split())  # 개수, 사이즈
box = list(map(int, input().split()))  # 상자들의 무게 중심
dp = [0 for _ in range(n)]

result = True
s = 0

for i in range(n-1,0,-1):
    s += box[i]
    if box[i - 1] - l < s / (n - i) < box[i - 1] + l:
        result = True
    else:
        result = False
        break

if result == True:
    print('stable')
else:
    print('unstable')