# n = int(input())
# card = []
# for i in range(1, n+1):
#     card.append(i)
# card.sort()
#
# while len(card) != 1:
#     card.pop(0)
#     card.append(card.pop(0))
#
# print(card[0])

from collections import deque

n = int(input())
cards = deque(range(1, n+1))

while len(cards) > 1:
    cards.popleft() # 가장 위의 카드 버리기
    cards.append(cards.popleft()) # 가장 위의 카드 맨 아래로 옮기기

print(cards[0])
