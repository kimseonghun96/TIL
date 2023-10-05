import sys

input = sys.stdin.readline

def factorial(N):
    num = 1
    for i in range(1, N+1):
        num *= i
    return num


T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    ans = factorial(M) // (factorial(N) * factorial(M-N))
    print(ans)

# mCn 으로 표현할 수 있고 이는 m! 을 (m-n)!n! 으로 나눈 값