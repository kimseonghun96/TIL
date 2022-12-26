# 1. UP는 올라가고 있는지 내려가고 있는지를 의미한다.
# 2. 첫 봉우리는 올라가고 있다는 것을 가정한다고 하였으니, 일단 UP = True로 시작한다.

# < 루틴 >
# 3. 지금 밟고 있는 idx의 값이 다음 idx의 값보다 작으면 올라가는 것이므로 UP를 True로 변경한다.
# 4. 지금 밟고 있는 idx의 값이 다음 idx의 값보다 크면 내려가고 있는 것이다.
#     -> 이때, UP가 True 라면, 올라갔다가 내려가는 것이므로 봉우리 count 를 += 1 해준다.
#     -> 이후 UP = False로 바꾸고, UP == False 인 상태에서 다시 내리막을 만나면 무시한다.
# 5. 높이가 같으면 그냥 pass 시키도록 범위를 지정해주지 않는다.
# < 루틴 종료 >

# 낚시 포인트
# 1. 높이가 0일 경우, 봉우리가 아니지 않니?
# 2. 높이 같을 경우를 체크 해줬니?
# 3. 봉우리 개수 자체가 0인 경우는 체크 했니?
# 4. 패딩 안하고 하면 큰 코 다친다? (양단의 값을 0으로 주거나 UP 기반으로 첫 값 True로 주는 경우, 요주의)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    height_list = [0] + list(map(int, input().split())) + [0]
    count = 0
    UP = True
    for checking in range(N+1):
        if height_list[checking] < height_list[checking+1]:
            UP = True
        elif height_list[checking] > height_list[checking+1]:
            if UP:
                count += 1
                UP = False
    print(f'#{tc} {count}')

"""
반례 모음
[테케]. All in one
5
0

1
0
5
1 1 1 1 1
7
0 5 1 3 4 2 0
20
4 5 2 2 4 3 2 3 3 4 5 7 5 3 5 3 1 3 3 3

[답]. All in one 답
#1 0
#2 0
#3 1
#4 2
#5 5
"""