# import heapq
#
# heap = []
#
# heapq.heappush(heap, 10)
# heapq.heappush(heap, 50)
# heapq.heappush(heap, 20)
#
# print(heap)
# print(heapq.heappop(heap))
# print(heap)


# 10과 가까운 우선순위 q
import queue

# Priority Queue 생성
priority_queue = queue.PriorityQueue()

# 1부터 10까지의 숫자를 5와의 거리를 기준으로 추가
target_number = 5
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    distance = abs(number - target_number)  # 5와의 거리 계산
    priority_queue.put((distance, number))  # 거리를 우선순위로 사용하여 추가

# 숫자를 거리에 따라 출력
while not priority_queue.empty():
    distance, number = priority_queue.get()
    print(f"{number} (거리: {distance})")