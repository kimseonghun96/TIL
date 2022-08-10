

'''
# 인덱스
-인덱스라는 용어는 Database에서 유래했으며, 테이블에 대한 동작 속도를
높여주는 자료 구조를 일컫는다. Database 분야가 아닌 곳에서는 Look up table
등의 용어를 사용하기도 한다
- 인덱스를 저장하는데 필요한 공간은 보통 테이블을 저장하는데 필요한
디스크 공간보다 작다. 왜냐하면 보통 인덱스킄 키-필드만 갖고 있고, 테이블의
다른 세부 항목들은 갖고 있지 않기 때문이다.
-배열을 사용한 인덱스
*대량의 데이터를 매번 정렬하면, 프로그램의 반응은 느려질 수 밖에 없다. 이러한 대량 데이터의
성능 저하를 문제를 해결하기 위해 배열 인덱스를 사용할 수 있다.

'''
'''
선택 정렬
-주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식
앞서 살펴본 셀렉션 알고리즘을 전체 자료에 적용한 것이다.

-정렬과정
주어진 리스트 중에서 최소값을 찾는다.
그 값을리스트의 맨 앞에 위치한 값과 교환한다.
맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복한다.
-시간 복잡도
O(n2)

정렬과정 
1.주어진 리스트에서 최소값을 찾는다.
minIdx = 0 #0번째 자리를 최소값으로 예상
for i in range(1, n-1)
    if A[i] < a[minIdx]
        minIdx <- i
A[0] <-> A[minIdx]

2. 리스트의 맨 앞에 위치한 값과 교환한다.
minIdx <- 1
for i in 2 -> N -1

3. 미정렬 리스트에서 최소값을 찾는다
4 리스트의 맨 앞에 위치한 값과 교환하다.

선택 정렬 알고리즘
def SelectionSort(a[], n)
    for i from 0 to n-2
        a[i], ....,a[n-1] 원소 중 최소값 a[k] 찾음
        a[i]와 a[k] 교환
        
구체적으로 표현
def selectionSort(a, N) :
    for i in range(N-1)       #구간시작
        minIdx = i            #기준시작
        for j in range(i+1, N) :    #바꾸는 과정
            if a[minIdx] > a[j]
                minIdx = j
        a[i], a[minIdx] = a[minIdx], a[i] #교환
        
 '''
#  #선택정렬
# arr = [7, 2, 5, 3, 4, 6]
# N = len(arr)
#
# for i in range(N-1):
#     minIdx = i # 구간의 맨 앞을 최소값으로 가정
#     for j in range(i+1, N): #실제 최소값 인덱스 찾기
#         if arr[minIdx] > arr[j]:
#             minIdx = j
#     arr[minIdx], arr[i] = arr[i], arr[minIdx] #최소값을 구간 맨 앞으로
# print(arr)

'''
셀렉션 알고리즘
-저장되어 있는 자료들로부터 k번째로 큰 혹은 작은 원소를 찾는 방법을 셀렉션 알고리즘이라 한다.
*최소값, 최대값 혹은 중간값을 찾는 알고리즘을 의미하기도 한다.

-선택 과정0
*셀렉션은 아래와 같은 과정을 통해 이루어진다
정렬 알고리즘을 이용하요 자료 정렬하기
원하는 순서에 있는 원서 가져오기
'''
#행의 합 구하기

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

s = 0
for i in range(N):
    for j in range(N):
        s += arr[i][j]
print(s)
