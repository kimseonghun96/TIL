T = 10

for tc in range(1, T+1):
    n = int(input())
    buildings = list(map(int, input().split()))
    ans = 0
    for i in range(2, n-2):
        value = 0
        if buildings[i] > 0:
            if buildings[i] == buildings[i+1] and buildings[i] == buildings[i+2]:
                pass
            elif buildings[i] > buildings[i-1] and buildings[i] > buildings[i-2] and buildings[i] > buildings[i + 1] and buildings[i] > buildings[i + 2]:
                max_building = max(buildings[i -1], buildings[i - 2], buildings[i + 1], buildings[i +2])
                value = buildings[i] - max_building
                ans += value

    print(f'#{tc} {ans}')

# import sys
# sys.stdin = open('test_input.txt')
#
# T = 10
# for tc in range(1, T+1):
#     N = int(input())
#     box = list(map(int, input().split()))
#     # print(box)
#     answer = 0
#     for i in range(2, N-2):
#         value = 0
#         if box[i] > 0:                          # box[i]가 0보다 작을 때는 제외
#             if box[i] == box[i+1] and box[i] == box[i+2]:              # 두 칸 차이 값이 같다면
#                 pass                            # 그냥 진행
#
#             elif box[i] > box[i - 1] and box[i] > box[i - 2] and box[i] > box[i + 1] and box[i] > box[i + 2]:        # 빼야될거 중에서 가장 큰 걸 빼기 위해 솔트 씀
#                     sort_box = [box[i - 1], box[i - 2], box[i + 1], box[i + 2]]
#                     sort_box.sort ()
#                     value = box[i] - sort_box[-1]
#                     answer += value
#
#
#     print(f'#{tc} {answer}')