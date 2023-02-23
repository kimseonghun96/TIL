def rev(n):
    n = list(str(n))    #reverse를 사용하기 위하여 문자열로
    n.reverse()
    n = int("".join(n)) # 다시 정수형으로 반환 모두 이어붙인 상태로
    return n

x, y = map(int, input().split())
x = rev(x)
y = rev(y)
print(rev(x+y))