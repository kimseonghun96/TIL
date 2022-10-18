# 행 우선 순회로 인덱스 만들 수 있는지
# 열로 만들 수 있는 지

# #리스트 안의 값
arr = [1, 2, 3, 4]
arr_sum = 0
for vla in arr:
    arr_sum = arr_sum + vla  #오른쪽이 수식
print(arr_sum)


#행 우선 탐색
N = 4
arr = [[1, 2, 3, 4],  #리스트 안의 리스트 인덱스를 2개 사용
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]

#len(arr) ==> 4
for i in range(len(arr)):  #range(N) 사용 가능
    #arr[i]
    for j in range(len(arr[i])): #rnage(N)사용가능
        print(arr[i][j], end=' ')
    print()


# 다음 100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.
#
# 다음과 같은 5X5 배열에서 최댓값은 29이다.

N = 4
arr = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]

for i in range(N):
    row_sum = 0                         #각 행의 시작할 때 초기화하는 변수 만듬 포문 안에 넣으면 저기를 지나갈때 초기화 되기때문에 합이 더해지지 않음

    for j in range(N):
        row_sum += arr[i][j]            #arr[i]의 행의 합이 row_sum에 저장된 상태
    print(row_sum)

row_sum = 0
for i in range(N):
    for j in range(N):
        row_sum += arr[i][j]            #arr[i]의 행의 합이 row_sum에 저장된 상태
    print(row_sum)

arr = [1, 2, 3, 4, 5, 6, 7]
max_val = arr[0]                    #첫번째 값을 가장 큰 값으로 지정
for i in range(1, len(arr)):        #비교 해서 더 크면 교환
    if max_val < arr[i]:
        max_val = arr[i]


# #대각
# arr = [[0]*5 for _ in range(5)]
# for i in range(5):
#     arr[i][i] = 1
#
# #대각 반대
# for i in range(5):
#     arr[i][4-i] = 2
# for line in arr:
#     print(*line)