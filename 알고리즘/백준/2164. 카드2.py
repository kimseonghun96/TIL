

from collections import deque

n = int(input())
cards = deque(range(1, n+1))

while len(cards) > 1:
    cards.popleft() # 가장 위의 카드 버리기
    cards.append(cards.popleft()) # 가장 위의 카드 맨 아래로 옮기기

print(cards[0])
