# 처음에 a를 b로 나눠 나머지를 a에 담는다. (1의 자릿수)
#  n - 1을 반복하여 나눗셈을 구현한다. (소수 n-1번째 자리까지 나눔)
# 마지막 나눗셈의 몫을 출력한다. (n번째 자리 수를 나눈 몫을 출력)

A, B, N = map(int, input().split())

A = (A % B)
for i in range(N - 1):
    A = (A * 10) % B

result = (A * 10) // B

print(result)