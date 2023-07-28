# 연속하는 P일 중, L일 동안만 사용할 수 있다. V일 짜리 휴가 시작
# 단순 계산 문제인데
# V % P > L 이 경우를 생각 못해서 시간 좀 걸림

tc = 1
while True:
    L, P, V = map(int, input().split())
    if L == 0:
        break

    if V % P > L:
        print(f'Case {tc}:', (((V // P) + 1) * L ) )
    else:

        print(f'Case {tc}:',((V // P) * L) + (V % P))
    tc += 1
