# 먼저 학생 수 +2 한 리스트를 만들고
# 졸고 있는 학생의 인덱스 체크
# 졸고 있는 학생을 제외한 배수 출석체크
# 구간합 졸고있는 학생 다음도 체크 ㄴㄴ

import sys
input = sys.stdin.readline

n, k, q, m = map(int, input().split())

sleep = [False for _ in range(n+3)]

# 자고 있는 학생 인덱스 체크
for i in map(int, input().split()):
    sleep[i] = True

check = [1 for _ in range(n+3)]

for i in map(int, input().split()):
    if sleep[i] != False:  # 학생이 자고 있다면
        continue           # 다음

    for j in range(i, n+3, i): # 그 배수를 체크하면서도
        if sleep[j] != False:  # 학생이 자고 있다면
            continue           # 다음

        check[j] = 0           # 출석체크 해줌

sum_ = 0                       # 누적합 할거임
check[2] = 0                   # 시작 값 0

for i in range(3, n+3):
    if check[i] != 0:          # 출석되지 않았다면
       sum_ += 1               # 1 증가시켜주고

    check[i] = sum_            # 그 값을 순서에 저장

for _ in range(m):
    s, e = map(int, input().split())
    print(check[e] - check[s-1]) # 구간의 값을 구해줌