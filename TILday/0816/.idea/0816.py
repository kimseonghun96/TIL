'''
# 3143. 가장 빠른 문자열 타이핑

#테스트 케이스 수와 문자열 A, B를 입력받음
T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    len_A = len(A)
    len_B = len(B)
    i = 0
    key = 0
    # A를 타이핑하며 B의 첫글자와 같은 글자가 나오면 B의 길이만큼 잘라서 B와 같은지 확인
    # 같다면 입력값 1을 증가시키고 다음 입력 글자를 B의 길이만큼 넘어간다
    # 아니라면 입력값 1을 증가시키고 다음 글자를 확인

    while i < len_A:       #i가 len_A길이보다 작을 때
        if A[i] == B[0]:            #A의 글자중 B의 첫글자와 같은 글자 발견

            if A[i:i+len_B] == B:       # A에서 B의 길이 만큼 잘라서 B와 같은지 확인
                key += 1                # 같다면 입력값을 1 증가하고
                i += len_B              # 다음 입력 글자를 B의 길이 만큼 넘어간다.

            else:                       # 아니라면
                key += 1                # 입력값을 1 증가하고
                i += 1                  # 다음 입력 글자를 확인

        else:                        # 아니라면
            key += 1                 # 입력값을 1 증가하고
            i += 1                   # 다음 입력 글자를 확인

    print(f'#{tc} {key}')
'''

'''
# 4861. [파이썬 S/W 문제해결 기본] 3일차 - 회문

문제 풀이: 길이가 M인 회문을 찾아 출력해야된다. 가로와 세로가 있을 수 있기 때문에 두가지 모두 찾아 저장해야됨.

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())   # N*N 배열에서 길이가 M인 회문 찾기
    temp = [list(input()) for _ in range(N)]   # N*N 배열 만들기
    # for _ in range(N):
    #     temp.append(list(input()))

    zip_temp = list(zip(*temp))          # 세로 회문 확인을 위한 전치

    answer = ''            # 회문 저장소

    for i in range(N):
        for j in range(N-M+1):          # 만약 N=20, M=13 이라면, [0:13]에서 [7:20]까지니까 N-M+1이어야함.
            if temp[i][j:j+M] == temp[i][j:j+M][::-1]:  # 가로를 돌다가 회문을 찾고
                answer = temp[i][j:j+M]                # 가로 회문 저장
            if zip_temp[i][j:j+M] == zip_temp[i][j:j+M][::-1]:  # 세로를 돌다가 회문을 찾고
                answer = zip_temp[i][j:j+M]                    # 세로 회문 저장
    answer = ''.join(answer)      # 리스트를 문자열로 합쳐서 반환
    print(f'#{tc} {answer}')
    # print('#{} {}'.format(tc, ''.join(answer)))
'''
'''
# 4864_문자열 비교

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    len_str1 = len(str1)            #str1의 문자열 길이
    len_str2 = len(str2)            #str2의 문자열 길이
    box = (len_str2 - len_str1 + 1) #겹치는 것이 없을 경우 len_str2 끝에서 len_str1 전까지만 알아보기 위해
    i = 0
    answer = 0         #초기값 0 겹치는게 없다면 0으로 출력됨

    while i < box:             #str2 문자열 0부터 시작
        if str2[i] == str1[0] and str2[i:i + len_str1] == str1:
        #str2[i]의 요소와 str 첫번째 요소가 같을 경우
        #str2 i부터 len_str1길이의 값이 str1과 같을 경우
            answer = 1          # answer 1출력
            break


        i += 1                      # 다음 입력 글자를 확인

    print(f'#{tc} {answer}')
    
'''
'''
# 4864_문자열 비교

T = int ( input () )
for tc in range ( 1, T + 1 ):
    str1 = input ()
    str2 = input ()

    len_str1 = len ( str1 )  # str1의 문자열 길이
    len_str2 = len ( str2 )  # str2의 문자열 길이
    box = (len_str2 - len_str1 + 1)  # 겹치는 것이 없을 경우 len_str2 끝에서 len_str1 전까지만 알아보기 위해
    i = 0
    answer = 0  # 초기값 0 겹치는게 없다면 0으로 출력됨

    while i < box:  # str2 문자열 0부터 시작
        if str2[i] == str1[0] and str2[i:i + len_str1] == str1:
            # str2[i]의 요소와 str 첫번째 요소가 같을 경우
            # str2 i부터 len_str1길이의 값이 str1과 같을 경우
            answer = 1  # answer 1출력
            break

        i += 1  # 다음 입력 글자를 확인

    print ( f'#{tc} {answer}' )


# 틀린 거 break 위치 확인

# 4864_문자열 비교

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    len_str1 = len(str1)            #str1의 문자열 길이
    len_str2 = len(str2)            #str2의 문자열 길이
    box = (len_str2 - len_str1)
    i = 0
    answer = 0         #초기값 0 겹치는게 없다면 0으로 출력됨

    while i < box:             #str2 문자열 0부터 시작
        if str2[i] == str1[0]:      #str2[i]의 요소와 str 첫번째 요소가 같을 경우
            if str2[i:i+len_str1] == str1: #str2 i부터 len_str1길이의 값이 str1과 같을 경우
                answer = 1          # answer 1출력
            break                   # 뒤에 겹치는 것이 있을 수 있기 때문에 처음에 발견했을 때 멈춤

        i += 1                      # 한번 돌 때마다 i 수 올림

    print(f'#{tc} {answer}')
'''

'''
글자수

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    max_word = 0
    for i in str1:

        max_word = 0
        for i in str1:  # str1을 순회
            if str2.count(i) > max_word:  # str1의 문자가 str2에 몇 개있는지 확인 후 가장 많은 i의 수를
                max_word = str2.count(i)  # max_word에 저장

    print (f'#{tc} {max_word}')
'''