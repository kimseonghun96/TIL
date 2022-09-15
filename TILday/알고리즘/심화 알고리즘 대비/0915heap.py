'''
힙 - 완전 이진트리여야 함
최소 힙 : 완전 이진트리이고 젤 위가 젤 작아야됨
최대 힙 : 완전 이진트리이고 젤 위가 젤 커야됨
'''
#최소힙
heap = ['최소합:']

def heap_push(item):
    heap.append(item) #완전 이진트리니까 맨끝에 +

    child = len(heap) - 1   # child의 인덱스
    parent = child // 2     # parent의 인덱스

    # 루트노드가 아니고, 위에 봤는데더 큰 경우에 계속 돈다.
    while parent and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent
        parent = child//2


def heap_pop():
    if len(heap) == 1: # 없을때 뽑지 않는 장치
        return
    result  = heap[1]
    item = heap.pop()
    heap[1] = item
    parent = 1 # 루트부터 시작하니까 1
    child = parent*2
    if child+1 <= len(heap)-1: # 오른쪽 노드가 트리 안에 존재하고 +
        if heap[child] > heap[child+1]:    # 왼쪽이 더 크면 최소힙으로서는
            child += 1      # 오른쪽으로 내려가게 하는 것이 맞음

        # 이번에는 아래로 내려가는거니까 오른쪽 노드가 존재할때까지 +
        # 최소힙 유지를 위해 필요할때까지!
        while child <= len(heap) - 1 and heap[parent] > heap[child]:
            heap[parent], heap[child] = heap[child], heap[parent]
            parent = child  # 이번에는 내려가는거니까 반대
            child = parent * 2  # 일단 이번에도 왼쪽이라고 가정해봄

            if child + 1 <= len(heap) - 1:  # 아까 그 로직 반복
                if heap[child] > heap[child + 1]:
                    child += 1

        return result

    heap_push(33)
    print(heap)
    heap_push(12)
    print(heap)
    heap_push(7)
    heap_push(19)
    heap_push(21)
    print(heap)
    heap_push(5)
    print(heap)
    heap_push(8)
    print(heap)
    print(heap_pop())
    print(heap)
    print(heap_pop())
    print(heap)
    print(heap_pop())
    print(heap)
    print(heap_pop())
    print(heap)
    print(heap_pop())
    print(heap)
    print(heap_pop())
    print(heap)




    return result
