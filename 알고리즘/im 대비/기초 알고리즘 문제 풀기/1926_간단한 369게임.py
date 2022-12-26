T = int(input())
for i in range(1, T+1): # 1 ~ 100
    
    i = str(i)    #count함수 쓰기 위해 문자열로
    print(i)

    #3, 6, 9 위치를 찾아줌 있으면 1 없으면 0
    clap = i.count('3') + i.count('6') + i.count('9')
    # print(clap) 

    # 그 자리가 0일 경우 엔 그대로 출력
    if clap == 0:
        print(i, end=' ')
    # 그자리가 1일경우엔 '-'으로 변환 출력
    else:
        print("-" * clap, end=' ')