#피보나치 수열
d, k = map(int, input().split())

#fibo(d-1)*a + fibo(d)*b
#K = ax + by

x = 1
y = 0
for i in range(d-1):
    x, y = y, x+y
for a in range(1, 100000):
    if (k - (x*a)) % y == 0:
        print(a, (k - (x*a))//y, sep="\n") #출력 시 값 사이에 문자를 넣기
        break