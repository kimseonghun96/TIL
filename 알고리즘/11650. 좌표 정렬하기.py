# 인덱스 비교


N = int(input())

people = []

for _ in range(N):
  x, y = map(int, input().split())
  people.append((x, y))

rank = []
for i in people:
  temp = 1
  for j in people:
    if i[0] < j[0] and i[1] < j[1]:
      temp += 1
  rank.append(temp)

print(*rank)