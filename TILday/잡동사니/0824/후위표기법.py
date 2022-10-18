# 연습문제 1 - 후위 표기법
# T = int(input())
# for tc in range(1, T+1):
#     N = input()
#     push_list = ['+', '-', '*', '/']
#     stack = []
#     print(f'#{tc}', end=' ')
#     for i in N:
#         if i in push_list:
#             stack.append(i)             # 연산자 먼저 담고
#         else:
#             print(i, end='')            # 숫자는 바로 출력
#     for i in range(len(stack)):
#         print(stack.pop(), end='')      # 연산자 마지막부터 출력
#     print()    #한칸 띄우는 거

# 연습문제 2 - extra
'''
)를 만나면 있는거 다 출력
마지막에 있는 거 출력
'''

# T = int(input())
# for tc in range(1, T+1):
#     N = list(input())
#     push_list = ['+', '-', '*', '/']
#     a =[] # 연산자 넣을 곳
#     stack = []
#     print(f'#{tc}', end=' ')
#     for i in N:
#         stack.append(i)
#         if stack[i] == '+' and '-' and '*' and '/':  # 스택의 요소 중 연산자와 같은 것들은 a메 담음
#             a.append(i)
#         for j in stack:
#             if stack[j] == a[i]:
#                 print(stack.pop(), end='')      # 연산자 마지막부터 출력
#             print()    #한칸 띄우는 거

            # 내일 물어보기