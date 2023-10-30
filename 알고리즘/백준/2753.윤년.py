# 윤년 시리즈 풀어보기

N = int(input())
if N % 4 == 0 and N % 100 != 0 or N % 400 ==0:
    print(1)
else:
    print(0)
