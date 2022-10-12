'''
1
5 2
1 3
2 4
'''
# 상자의 개수와 몇번 작업을 하는지 받는다.
# 0이 적혀 있는 리스트를 만들고
# Q번 돌면서 L,R의 값을 받는다(범위)
# L,R의 범위 만큼의 box[idx]를 i번으로 바꾼다.
# 그 값을 박스에 담아 출력!


T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    box = [0]*(N+1)
    result = []
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L, R+1):
            box[j] = i

    for k in range(1, len(box)):
        result.append(box[k])

    print(f'#{tc}', *result)
