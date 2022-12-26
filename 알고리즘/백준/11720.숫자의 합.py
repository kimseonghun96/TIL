N = int(input())
numbers = input()
num_list = list(map(int, numbers))
# print(sum(num_list))
answer = 0
for i in range(N):
    answer += num_list[i]

print(answer)

