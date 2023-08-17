# 상근이 정확하게 N 배달 해야함
# 공장엔 3 or 5
# 최대한 적은 봉지를 가져가려면 5의 봉지가 많아야함

import sys
input = sys.stdin.readline
N = int(input())

# 일단 5의 봉지로 나눠보자
check5 = N // 5  # 몫
temp5 = N % 5    # 나머지
check3 = 0   # 3의 몫을 담자

while check5 >= 0:
    if N == 5:
        break
    elif N == 3:
        check3 = 1
        break
    elif temp5 == 0:
        break
    elif temp5 != 0 and temp5 % 3 == 0:
        check3 = temp5 // 3
        temp = 0
        break
    else:
        check5 -= 1
        temp5 += 5

print(check3 + check5)




