N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = 0
for i in range(N):
    sum_list = 0
    sum_list = A.index(min(A)) * B.index((max(B)))
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))
    answer += sum_list
print(answer)