import sys

input = sys.stdin.readline

A = int(input())
T = int(input())
say = int(input())

bundegi = [] # 번, 데기를 외친 횟수,
bun, degi = 1, 1
turn = 0 # 구하고자 하는 구호의 차례가 이번 턴에 속해있는지를 확인

while True:
    prev_n = bun #이전 회차에 번 데기를 누적 몇 번 외쳤는지 저장
    turn += 1
    for _ in range(2):
        bundegi.append((bun, 0))
        bun += 1
        bundegi.append((degi, 1))
        degi += 1

    # 번 연속 turn + 1 번
    for _ in range(turn+1):
        bundegi.append((bun, 0))
        bun += 1

    # 데기 연속 turn + 1 번
    for _ in range(turn+1):
        bundegi.append((degi, 1))
        degi += 1

    # 이번 턴에 구하고자하는 구호가 있다면
    if prev_n < T <= bun:
        # print(bundegi)
        # print(bundegi.index((T, say)))
        print(bundegi.index((T, say)) % A)
        # 번, 데기를 외친 총 누적 수를 게임 참여 인원수로 나눈 나머지가 구하고자 하는 사람의 번호
        break
