# n = int(input())

# six = [666]
# ans = []
# if n-1 == 0:
#     ans.append(*six)
#     print(int(''.join(map(str, ans))))
#
# elif n-1 != 0:
#     six.append(n-1)
#
#     ans.append(six.pop())
#     ans.append(*six)
#     print(int(''.join(map(str, ans))))

n = int(input())

a = 666
cnt = 0

while n:
    if "666" in str(a):
        n -= 1
    a += 1

print(a-1)