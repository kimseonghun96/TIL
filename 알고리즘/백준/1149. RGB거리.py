import sys
read = sys.stdin.readline

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
# print(house) = [[26, 40, 83], [49, 60, 57], [13, 89, 99]]

#대각선 위에 있는 숫자들 중 작은 수를 나와 더한다.
for i in range(1, N):
    house[i][0] += min(house[i-1][1], house[i-1][2])
    house[i][1] += min(house[i-1][0], house[i-1][2])
    house[i][2] += min(house[i-1][0], house[i-1][1])

# print(house) = [[26, 40, 83], [89, 86, 83], [96, 172, 185]]
print(min(house[-1]))
print(house)