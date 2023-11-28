# replace() 함수는 왼쪽부터 해당하는 문자열을 찾아서 치환해주는 함수.
# 먼저 입력값을 board 변수에 저장합니다. 그리고 replace() 함수를 2번 호출.
# 왼쪽부터 모든 'XXXX'를 'AAAA'로 치환하고, 바뀐 문자열에서 남은 'XX'를 모두 'BB'로 치환
# 문자열 체크



import sys

input = sys.stdin.readline

board = input().rstrip() + '.'
ans = ''

print(board)

for i in board:
    if len(i) % 2 != 0:
        print(-1)
        break
    else:
        while len(i) >= 4:
            ans += 'AAAA'
        if len(i) == 2:
            ans += 'BB'


    print(ans)