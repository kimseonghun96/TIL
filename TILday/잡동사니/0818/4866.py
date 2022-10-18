T = int(input())
for tc in range(1, T + 1):
    bracket = input()
    left_bracket = []
    result = 1          # 초기 설정을 1
    for i in bracket:
        # ( 이나 {이면 left_bracket 에 담음
        if i == '(' or i == '{':
            left_bracket.append(i)
        # result 가 0이 나올 모든 경우의 수 확인
        elif i == ')' or i == '}':    # ) 이나 }이 나오면 (나 { 전에 나왔는지 확인
            if len(left_bracket) == 0:        # 전에 '(','{' 이 안나 왔으면 맨 짝이 안 맞음
                result = 0
                break                       # 더 이상 볼 필요 없음
            # 적절하게 짝이 이루어졌는지 확인
            elif i == ')' and left_bracket.pop() != '(':     # 마지막에 들어간 left_bracket 와 짝이 맞아야 됨 맞지않다면 0
                result = 0
                break
            elif i == '}' and left_bracket.pop() != '{':     # 마지막에 들어간 left_bracket 와 짝이 맞아야 됨 맞지않다면 0
                result = 0
                break
    # 괄호가 모두 짝이 맞게 닫혀서 left_bracket에 남아있는 것이 없는 지 확인 남아있는게 있다면 True 짝이 맞지 않다는 것이므로 result =
    if len(left_bracket):
        result = 0

    print(f'#{tc} {result}')

<틀린거>
# T = int(input())
# for tc in range(1, T+1):
#     bracket = input()
#     small_bracket = []
#     big_bracket = []
#
#     # 나누기 사용하자
#
#     for i in bracket:
#         if i in ('(', ')'):
#             small_bracket.append(i)  # '(', ')' 담고
#         elif i in ('{','}'):
#             big_bracket.append(i)       # '{', '}' 담고
#
#
#
#     if len(small_bracket) % 2 == 0 or len(big_bracket) % 2 == 0:     # 합친 걸 나누었을 때 0이 아니라면 짝이 맞지 않는 것이니까
#         print(f'#{tc} 1')
#
#     else:
#         print(f'#{tc} ')

    #반례 {(}) 일 때도 짝은 맞지만 짝이 아님
