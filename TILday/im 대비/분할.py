# 분할 ==> 조합과 관련이 있다.
# 주어진 전체 N개의 자료에서 2개 혹은 3개를 뽑는(선택하는) 모든 경우를 나열(생성)

# arr =['A', 'B', 'C']
# N = len(arr)

# # 중복 순열
# for i in range(N):          # i => 0 ~ N-1
#     for j in range(N):      # j => 0 ~ N-1
#         print(i, j, arr[i], arr[j])

# # 순열
# for i in range(N):          # i => 0 ~ N-1
#     for j in range(N):      # j => 0 ~ N-1
#         if i != j:
#             print(i, j, arr[i], arr[j])

#조합
# for i in range(N):          # i => 0 ~ N-1
#     for j in range(i+1, N):      # j => 0 ~ N-1
#         if i == j: continue
#         print(i, j, arr[i], arr[j])

N = 5
arr = [i for i in range(1, N+1)]

#   3구간으로 분할 => (0, i) (i, j) (j, N-1)
for i in range(1, N-2+1):
    for j in range(i+1, N -1 +1):
        print(arr[0:i], arr[i:j], arr[j:N])