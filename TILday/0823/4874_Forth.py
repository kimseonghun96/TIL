# t = int ( input () )
# for tc in range ( 1, t + 1 ):
#     s = list ( map ( str, input ().split () ) )
#
#     stack = []
#     for n in s:
#         if n == '.':                                        # 먼저 .를 만나면 출력한다.
#             if len ( stack ) == 1:                          # stack에 남아있는 것이 1개일 경우
#                 print ( "#" + str ( tc ), stack.pop () )    # stack에 남아있는 것을 뽑아서 출력
#             else:                                           # 1개 이상일 경우 에러
#                 print ( "#" + str ( tc ), 'error' )
#         elif n.isdigit ():                                  # 숫자일 경우 추가
#             stack.append ( n )
#         else:                                               #숫자가 아닐 경우 연산자를 이용해 계산해야되는데
#             if len ( stack ) < 2:                           #스택에 숫자가 두개보다 적을 경우 연산을 할 수 없으므로, 에러
#                 print ( "#" + str ( tc ), 'error' )
#                 break
#             else:                                                   #각각에 맞는 연산을 계산한 후 출력
#                 b = int ( stack.pop () )
#                 a = int ( stack.pop () )
#                 if str ( a ).isalpha () or str ( b ).isalpha ():
#                     print ( "#" + str ( tc ), 'error' )
#                     break
#                 elif n == '+':
#                     stack.append ( a + b )
#                 elif n == '-':
#                     stack.append ( a - b )
#                 elif n == '/':
#                     stack.append ( int ( a // b ) )
#                 elif n == '*':
#                     stack.append ( a * b )



T = int(input())
for tc in range(1, T + 1):
    arr = list(input().split())
# print(arr)
    oper = '+-/*'   # 연산자들
    stack = []      # 숫자를 담을 stack
    for i in arr:   # 입력을 앞에서부터 하나씩 탐색
        if i == '.':
            if len(stack) == 1:                 # 먼저 .를 만났을 때 stack에 1개가 있다면
                print(f'#{tc} {stack.pop()}')
            else:
                print(f'#{tc} error')
            break
        elif i in oper:         # 연산자인 경우
            if len(stack) < 2:  # 연산을 하기 위해선 stack에 숫자가 2개 이상 있어야 한다.
                print(f'#{tc} error')   # 2개 이상 없다면 error
                break
            b = stack.pop()     # b와 a의 순서에 유의, 나중에 넣은 값이 연산할 때 뒤로 가게
            a = stack.pop()
            if i == '+':
                stack.append(a+b)
            elif i == '-':
                stack.append(a-b)
            elif i == '*':
                stack.append(a*b)
            else:
                stack.append(a//b)
        else:                   # 숫자인 경우 stack에 담는다.
            stack.append(int(i))