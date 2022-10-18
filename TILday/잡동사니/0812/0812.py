'''
faltten 높은 곳의 상자를 낮은 곳으로 옮겨야 한다. 이것을 평탄화 작업
평탄화를 수행하면 가장 높은 곳과 낮은 곳의 차이가 1 이내
횟수제한이 걸려있고 제한된 횟수 만큼 옮기는 작업을 한 후 최고점과 최저점의 차이를 반환하는
프로그램을 작성

평탄화 작업을 dump 라고 함 횟수 100이내로 제한

가장 먼저 받은 상자를 내림차순으로 정렬 -> 버블 정렬 사용
그럼 가장 앞쪽의 수 [0]가 제일 작고 [99]의 수가 제일 클 것
두 수의 차이가 2이 상일 경우 뒤 쪽의 상자는 하나 빼고 뒤쪽의 상자는 하나 옮기는
작업을 100만큼 해야함
#이 때 차이가 나지 않으면 다시 정렬 -> 그리고 또 작은 숫자와 큰숫자 비교
두 수의 차이가 1이 될 때 높은 수와 낮은 수의 차이를 출력
'''
import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    dump = int(input())  # 옮기는 수 받는 곳
    boxes = list(map(int, input().split()))      #박스를 리스트 형식을 나누어서 받음

    flag = True   #while도 멈추기 위해서
    while dump:
        if flag == False:
            break
        for i in range(99, 0, -1):         # 버블 정렬 횟수 100번
            for j in range(i):
                if boxes[j] > boxes[j+1]:  # i의 위치가 그 다음 위치인 i+1보다 클 경우
                    boxes[j], boxes[j+1] = boxes[j+1], boxes[j] #위치 변경 -> 오름차순으로 정렬

            if boxes[-1] - boxes[0] >= 2:   #가장 뒤 쪽에 있는 큰 수와 앞 쪽에 있는 작은 수의 차이가 1보다 클 경우
                boxes[-1] -= 1           # 큰 수의 박스를 하나 빼고
                boxes[0] += 1             # 작은 수의 박스를 하나 추가함
                dump -= 1                # 평탄화 작업 1번 줄어듬
                continue                 # 이 작업을 반복

            else:      #차이가 없다면 멈추고  최고값과 최저값의 차이를 출력함
                print(f'# {tc} {boxes[-1] - boxes[0]}')
                flag = False
                break
    # 위의 경우는 dump가 실행하기 전에 최소값과 최대값의 차이가 1이 날 때 출력하기 때문에
    # dump 횟수가 0일 경우도 만들어 줘야한다.

    if dump == 0:          # dump의 횟수가 0일 때
        for i in range(len(boxes)-1, 0, -1):   #버블 정렬을 다시 해준다.
            for j in range(i):
                if boxes[j] > boxes[j+1]:
                    boxes[j], boxes[j+1] = boxes[j+1], boxes[j]

        print(f'# {tc} {boxes[-1] - boxes[0]}')  #최대값과 최소값 출력

# 구간합
'''
N개의 정수가 들어 있는 배열에서  M개의 합을 계산하는 것
M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력
그러면 배열에서 i번째에서 M-1번째까지 합을 확인 하고 합을 답는 곳을 만듬
i+1 하고 다시 M-1번째까지 합 확인  이 합이 크다면 위치를 뒤 쪽으로
이렇게하면 가장 작은 합은 맨 앞으로
마지막에 [-1]과 [0]의 차를 출력한다.
'''

T = int ( input () )
for tc in range ( 1, T + 1 ):
    N, M = list ( map ( int, input ().split () ) )  # 정수의 개수 N, 구간의 개수 M을 받는곳
    num_list = list ( map ( int, input ().split () ) )  # N개의 정수 받는 곳
    sum_list = []  # 구간합의 리스트 모으는 곳

    for i in range ( N - M + 1 ):  # 구간합을 구하는 길이만큼 돔 (밖으로 나가지 않기 위해 범위 설정)
        sum_num = sum ( num_list[i:i + M] )  # 구간합을 구함
        sum_list.append ( sum_num )  # 구간합을 리스트에 추가함

    # 이제 구간합을 정렬할 거임
    for i in range ( len ( sum_list ) ):  # 구간합의 리스트의 길이만큼 도는데
        for j in range ( i + 1, len ( sum_list ) ):  #
            if sum_list[i] > sum_list[j]:
                sum_list[i], sum_list[j] = sum_list[j], sum_list[i]
    print ( f'#{tc} {sum_list[-1] - sum_list[0]}' )


'''
태보
얼굴을 기준으로 왼쪽 주먹 개수 오른쪽 주먹 개수를 구한다
'''



punch = input().split('(^0^)')  #(^0^) 하나밖에 없기 때문에 (^0^) 기준으로 리스트 두 개가 생김
for i in range(2):
    left = punch[0].count('@')
    right = punch[1].count('@')

print(left, right)




