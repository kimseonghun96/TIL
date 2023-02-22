n = int(input())

a = 0
b = 1
result = 0
while n:
    result = a + b
    a = b
    b = result
    n -= 1
    if n == 1:
        break

print(result)



# 시간 초과

# n = int(input())
#
# def pa(n):
#     if n <= 1:
#         return 1
#     return pa(n-1) + pa(n-2)
#
# print(pa(n-1))

# n = int(input())
#
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# print(fibonacci(n))

