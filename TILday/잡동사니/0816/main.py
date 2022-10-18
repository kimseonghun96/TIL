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
    # A를 타이핑하며 B의 첫글자와 같은 글자가 나오면 B의 길이만큼 잘라서 b와 같은지 확인
    # 같다면 입력값 1을 증가시키고 다음 입력 글자를 B의 길이만큼 넘어간다
    # 아니라면 입력값 1을 증가시키고 다음 글자를 확인

    while i < len_A:
        if A[i] == B[0]:
            if A[i:i+len_B] == B:
                key += 1
                i += len_B
            else:
                key += 1
                i += 1
        else:
            key += 1
            i += 1
    print(f'#{tc} {key}' )
'''

'''
# 4861. [파이썬 S/W 문제해결 기본] 3일차 - 회문
 
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())   # N*N 배열에서 길이가 M인 회문 찾기
    arr = []
    for _ in range(N):
        arr.append(list(input()))

    zip_arr = list(zip(*arr))          # 세로 회문 확인을 위한 전치

    answer = 0

    for i in range(N):
        for j in range(N-M+1):          # 만약 N=20, M=13 이라면, [0:13]에서 [7:20]까지니까 N-M+1이어야함.
            if arr[i][j:j+M] == arr[i][j:j+M][::-1]:  # 가로를 돌다가 회문을 찾고
                answer = arr[i][j:j+M]                # 가로 회문 저장
            if zip_arr[i][j:j+M] == zip_arr[i][j:j+M][::-1]:  # 세로를 돌다가 회문을 찾고
                answer = zip_arr[i][j:j+M]                    # 세로 회문 저장
    answer = ''.join(answer)      # 리스트를 문자열로 합쳐서 반환
    print(f'#{tc} {answer}')
    # print('#{} {}'.format(tc, ''.join(answer)))
'''


