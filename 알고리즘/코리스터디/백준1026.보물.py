N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_list = sorted(A) #정렬하라고해서 함
# print(A_list[0])
answer = 0
for i in range(1, N+1):
    answer += A_list[0] * max(B) #가장 작은 것과 큰것을 곱함
    A_list.pop(0)
    B.pop(B.index(max(B)))

print(answer)


