'''
3
7 5
1 3 5 6 4 4 6
10 5
1 3 4 2 3 7 1 6 9 2
10 5
4 7 5 5 1 5 4 4 3 3
'''
# # 내장함수 사용해서 푼거
# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     arr = list(map(int, input().split()))
#     arr_sort = sorted(arr)  # 정렬
#     arr_set = set()         # 중복제거 를 위한 set
#     for i in range(len(arr_sort)):
#         arr_set.add(arr_sort[i]) # 더해줌
#     arr_set = list(arr_set)   # 다시 리스트화
#
#     print(f'#{tc} {arr_set[K-1]}')


# 카운팅을 해도 무방하지만
# 중복을 제거하고, 크기순으로 자료에 접근하기 위해
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    # 값의 범위 => 1~1000
    cnt = [0] * (1001)

    for val in arr:
        cnt[val] = 1

    ans = kth = 0
    for i in range(len(cnt)): # 1 ~ 1000
        if cnt[i] == 0: # 이면 그냥 패스
           pass
        else:
            kth += 1
            if kth == K:
                #i를 출력
                ans = i
                break
    print(f'#{tc} {ans}')
