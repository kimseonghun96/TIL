N = list(map(int, input().split()))
# print(N)
k = 0
for i in N:
    k += i**2
print(k%10)