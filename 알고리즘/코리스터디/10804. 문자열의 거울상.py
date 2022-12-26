'''
2
bdppq
qqqqpppbbd
'''

T = int(input())
for tc in range(1, T+1):
    word = list(input())
    drow = word[::-1]   # 거울에 비치면 일단 뒤집힘
    mirror = ''
    for i in range(len(drow)):  # 거울에 비칠 때 바뀌는 mirror에 문자를 저장해줌
        if drow[i] == 'q':
            mirror += 'p'
        elif drow[i] == 'p':
            mirror += 'q'
        elif drow[i] == 'b':
            mirror += 'd'
        else:
            mirror += 'b'

    print(f'#{tc} {mirror}')












