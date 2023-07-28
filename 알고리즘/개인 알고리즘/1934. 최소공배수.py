# 두개를 곱하고 약수를 만든  후
# 두 개와 나눠지는 처음의 수를 출력하면 될 듯?

T = int(input())

for tc in range(T):

    # 최대공약수
    def gcd(a, b):
        while b > 0:
            a, b = b, a % b
        return a

    # 최소공배수
    def lcm(a, b):
        return a * b // gcd(a, b)

    A, B = map(int, input().split())
    print(lcm(A, B))