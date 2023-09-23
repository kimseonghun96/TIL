import sys
import heapq

input = sys.stdin.readline

n = int(input())

heap = []

for _ in range(n):
    print(heap)
    X = int(input())
    if X == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-1 * heapq.heappop(heap))  # 양수로 뽑으려고, heapq.heappop(heap)는 가장 작은 걸 리턴
    else:
        heapq.heappush(heap, (-X))   # heapq를 활용하지만 이 함수는 min heap만을 지원한다. 그래서 음수로 만들어서 리스트에 넣음