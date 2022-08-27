dust = int(input())
if 0 <= dust <= 30:
    print('좋음')
elif 30 < dust <= 80:
    print('보통')
elif 80 < dust <= 150:
    print('나쁨')
elif 150< dust <=300:
    print('매우나쁨')
    if dust > 300:
        print('실외 활동을 자제하세요.')
else:
    print('값이 잘못되었습니다.')
