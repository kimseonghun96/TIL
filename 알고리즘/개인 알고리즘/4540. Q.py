datasets = int(input())  # 데이터셋의 개수를 입력받습니다.

for _ in range(datasets):
    m, n = map(int, input().split())  # 각 데이터셋의 m과 n 값을 입력받습니다.
    queueA = []  # 초기 큐 A를 나타내는 빈 리스트를 생성합니다.
    queueB = [None] * 20  # 큐 B를 나타내는 리스트를 생성하고, None으로 초기화합니다.
    moved = [0] * 20  # 각 아이템이 움직였는지 여부를 나타내는 리스트를 생성하고, 0으로 초기화합니다.

    queueA = input().split()  # 큐 A에 아이템들을 공백을 기준으로 분리하여 입력받습니다.

    for _ in range(n):
        source, target = map(int, input().split())  # 각 이동에 대한 정보를 입력받습니다.
        queueB[target - 1] = queueA[source - 1]  # 큐 A의 source 위치의 아이템을 큐 B의 target 위치에 넣습니다.
        moved[source - 1] = 1  # 해당 아이템이 움직였음을 표시합니다.

    nextslot = 0  # 다음 비어있는 슬롯의 위치를 나타내는 변수를 초기화합니다.
    for j in range(m):
        if not moved[j]:  # 아직 움직이지 않은 아이템일 경우
            while queueB[nextslot] is not None:  # 큐 B의 다음 슬롯이 비어있지 않을 때까지 반복
                nextslot += 1  # 다음 슬롯으로 이동합니다.
            queueB[nextslot] = queueA[j]  # 큐 A의 아이템을 큐 B의 비어있는 슬롯에 넣습니다.
            nextslot += 1  # 다음 비어있는 슬롯으로 이동합니다.

    print(' '.join(queueB[:m]))  # 큐 B의 처음부터 m까지의 아이템을 공백을 사이에 두고 출력합니다.
