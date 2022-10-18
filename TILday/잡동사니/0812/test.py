T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))     # 정수의 개수 N, 구간의 개수 M을 받는곳
    num_list = list(map(int, input().split())) # N개의 정수 받는 곳
    sum_list = []                              # 구간합의 리스트 모으는 곳
    
    for i in range(N-M+1):                        # 구간합을 구하는 길이만큼 돔 (밖으로 나가지 않기 위해 범위 설정)
        sum_num = sum(num_list[i:i+M])            # 구간합을 구함
        sum_list.append(sum_num)                  # 구간합을 리스트에 추가함
    
    #이제 구간합을 정렬할 거임
    for i in range(len(sum_list)):             #구간합의 리스트의 길이만큼 도는데
        for j in range(i+1, len(sum_list)):     
            if sum_list[i] > sum_list[j]:      # i의 위치와 i+1의 위치를 비교 함
                sum_list[i], sum_list[j] = sum_list[j], sum_list[i] #조건 충족한다면 위치 바꿈
    print(f'#{tc} {num_list[-1]-num_list[0]}')