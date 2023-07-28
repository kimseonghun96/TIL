A, B, V = list(map(int, input().split()))

height = A - B

if (V - A) % height == 0:
    print(((V - A) // height) + 1)
else:
    print(((V - A)// height) + 2)

