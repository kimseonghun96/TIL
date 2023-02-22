# def a(n):
#     if n <= 1:
#         return 1
#     return n * a(n-1)
#
# print(a(5))

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

print(gcd(192, 162))