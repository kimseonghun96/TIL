# 그냥 덧셈 뺄셈,,

T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    hour = A+B
    if hour < 24:
        print(f'#{tc} {hour}')
    elif hour == 24:
        print(f'#{tc} 0')
    elif hour > 24:
        print(f'#{tc} {hour-24}')




    # dddddddddddd