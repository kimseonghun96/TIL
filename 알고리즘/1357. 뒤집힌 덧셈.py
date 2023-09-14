# ::-1은 뒤집는 거

X, Y = map(int, input().split())

def Rev_a(X):
    a = int(str(X)[::-1])
    return a

def Rev_b(Y):
    b = int(str(Y)[::-1])
    return b


print(Rev_a(Rev_a(X)+Rev_b(Y)))
