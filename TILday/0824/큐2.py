#개수가 많으면 느려진다.

from collections import deque

q = deque()

q.append(10)
q.append(20)
q.append(30)

print(q.popleft())
print(q.popleft())
print(q.popleft())
