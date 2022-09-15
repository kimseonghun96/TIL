N = int(input())
num = map(int, input().split())
answer = sorted(num)
print(answer[0], answer[-1])