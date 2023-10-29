# 문자열ㅇ만 체크하면됨

T = int(input())
for tc in range(1, T+1):
    N, str = input().split()
    N = int(N)
    word = ''
    for i in str:
        word += i*N

    print(word)
