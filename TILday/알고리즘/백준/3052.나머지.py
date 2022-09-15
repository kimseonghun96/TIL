A = list(int(input()) for _ in range(10))

# print(A)
answer = []
for i in range(len(A)):
    answer.append(A[i]%42)
answer = set(answer)
print(len(answer))