# 연습문제 1

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # n by n
    arr=[list(map(int, input().split())) for _ in range(N)] #다 도는 거
    dr = [-1, 1, 0, 0]  #방향이 상관없을 경우(4방향 다 볼 경우) #d = 델타 상, 하, 우, 좌
    dc = [0, 0, 1, -1]  # for 위에 적는 것이 좋다.

    answer = 0 # 합산 값

    for r in range(N):         # 2중 for 문 사용해서 전부 다 밟기
        for c in range(N):
            #각자 시행 횟수 안에서
            for i in range(4):  #다 밟으면서 4방향을 볼거임
                nr = r + dr[i]
                nc = c + dc[i]

                if nr < 0 or nr >=N or nc< 0 or nc >=N:  # 벽에 있는 요소는 인접한 요소가 없기 때문에 밖으로 나가면 안된다.
                    continue

                answer += abs(arr[r][c] - arr[nr][nc])  #abs 절대값
    print(f'# {tc} {answer}')

# 비트를 활용한 부분집합 구하기
letters = ['a', 'b', 'c']

for i in range(1 << len(letters)):  # 총 2³, 8개의 경우의 수 체크
    selected = []
    for j in range(len(letters)): # 셀로판지가 가야하는 길이는 3
        if i & (1 << j):  # 1칸씩 왼쪽으로 옮겨가며 총 3칸을 대조해본다.
            selected.append(letters[j])

    print(selected)

# []                | => (i = 0) => 0 0 0 => 공집합
# ['a']             | => (i = 1) => 0 0 1 => (j = 0)에서 걸려 'a'가 뽑힘
# ['b']             | => (i = 2) => 0 1 0
# ['a', 'b']        | => (i = 3) => 0 1 1
# ['c']             | => (i = 4) => 1 0 0 => (j = 2)에서 걸려 'c'가 뽑힘
# ['a', 'c']        | => (i = 5) => 1 0 1
# ['b', 'c']        | => (i = 6) => 1 1 0
# ['a', 'b', 'c']   | => (i = 7) => 1 1 1

#선택 정렬
nums = [10, 15, 2, 19, 6, 14]

for i in range(len(nums)-1):
    min_idx = i  # 일단 처음으로 들어오는 것이 가장 작다고 초기화해두고,

    for j in range(i+1, len(nums)): # 나 다음부터 보면서
        if nums[j] < nums[min_idx]:  # 나보다 작은애가 있으면
            min_idx = j  # 그 idx를 갱신!

    nums[i], nums[min_idx] = nums[min_idx], nums[i]  # 최종적으로 한번 스왑

print(nums)
