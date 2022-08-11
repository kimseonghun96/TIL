#아직 덜 완성됨

def binarySearch(N, key):  # N = 검색 대상 배열  key = 찾고자하는 대상
    start = 1  # 시작과 끝을 정함
    end = N
    cnt = 0
    while start <= end:  # =를 빼먹으면 start == end가 같을경우도 비교하기 때문에
        middle = (start + end) // 2  # 이진 검색을 하기 위한 중간지점
        if N[middle] == key:  # 검색 성공
            return cnt
        elif N[middle] > key:  # 찾고자 하는 것이 크다면
            end - middle  # 반대 쪽 지워버림
        else:
            start = middle  # 끝을 정했기에 넘어서면 start와 end 위치가 역전됨 실패
            cnt += 1  # 검색실패


T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())            #P는 크기고 인덱스 들어갈 수로 변환해서 넣어야됨
    if binarySearch(P, Pa) < binarySearch(P, Pb):
        print(f'# {tc} A')

    elif binarySearch(P. PA) > binarySearch(P, Pb):
        print(f'# {tc} B')

    else:
        print(f'# {tc} 0')
