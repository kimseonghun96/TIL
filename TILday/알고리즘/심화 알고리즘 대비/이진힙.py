'''
3
6
7 2 5 3 4 6
6
3 1 4 16 23 12
8
18 57 11 52 14 45 63 40
'''

def heap_make(idx):   # 힙만드는 거
    if heap[idx] < heap[idx//2]:
        heap[idx], heap[idx//2] = heap[idx//2], heap[idx]
        heap_make(idx//2) # 위치 이동



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nord = list(map(int, input().split()))
    heap = [0]
    idx = 0

    for i in nord:
        heap.append(i)
        idx += 1
        heap_make(idx)

    result = 0
    while idx > 0:
        idx //=2
        result += heap[idx]
    # idx = idx // 2
    print(f'#{tc} {result}')




def heap_push(item):
    heap.append(item)  # 완전 이진트리니까 맨끝에 +

    child = len(heap)-1
    parent = child // 2
    # 루트노드가 아니고, 위에 봤는데 더 큰 경우 계속 돎
    while parent and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]  # swap
        child = parent
        parent = child // 2

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    heap = ['최소힙 :']
# [1] 인풋 리스트를 모두 힙리스트에 추가
    for i in nums:
        heap_push(i)
# [2] 마지막 인덱스를 찾아서
    end_idx = len(heap) - 1
# [3] 부모(인덱스//2)를 구해서 더하기 루트까지 반복
    answer = 0
    while end_idx > 1:
        answer += int(heap[end_idx // 2])
        end_idx = end_idx // 2
    print(f'#{tc} {answer}')