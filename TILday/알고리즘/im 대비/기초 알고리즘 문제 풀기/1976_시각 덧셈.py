T = int(input())
hr = 0
mi = 0
for tc in range(1, T+1):
    num = list(map(int, input().split()))
    hr = num[0] + num[2]
    mi = num[1] + num[3]
    if mi > 59:
        mi -=60
        hr += 1

    if hr > 12:
        hr -= 12

    print(f'#{tc} {hr} {mi}')


