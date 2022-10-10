import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # 보석의 개수, 예산
    jewelry = list(map(int, input().split()))

    box = [4, 6, 7, 9, 11]  # 내가 모을 보석의 숫자들 배수도 가능

    new_box = []    # 내가 얻을 수 있는 보석만 모아두는 리스트(배수까지)
    for i in range(5):
        for j in range(1, 50):
            if 1 <= box[i] * j <= 100:          # 문제보면 100이하까지의 보석만 있음
                new_box.append(box[i] * j)

    real_box = []   # 쥬얼리 중에서 내가 수집하는 보석만 따로 다시 모음
    for i in range(N):
        if jewelry[i] in new_box:
            real_box.append(jewelry[i])

    sum_box = []  # 내가 가진 쥬얼리의 모든 합을 구함
    for i in range(1 << len(real_box)):  # 부분집합의 합 구하는 건데 노션 참고해서 같이 공부해야 할듯
        selected = []
        for j in range(len(real_box)):
            if i & (1 << j):  # 1칸씩 왼쪽으로 옮겨가며 대조해본다.
                selected.append(real_box[j])
        sum_box.append(sum(selected))

    # print(sum_box)
    ans = []                            # 모든 경우의 합 중에서
    for i in range(len(sum_box)):       # 50 이하의 것만 담음
        if sum_box[i] <= 50:
            ans.append(sum_box[i])
    # ans.sort()                          # 50에 가장 가까운 수는 맨 끝에 있을 것이므로
    #
    # print(f'#{tc}', ans[-1])          # 생각해보니 그냥 가장 큰 수 뽑으면 됨
    print(f'#{tc}', max(ans))


