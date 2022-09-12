A = int(input())
B = int(input())
C = int(input())
# print(N)
num = A * B * C
# print(num)
list_num = list(map(int, str(num))) #자연수 리스트로 담는 법
cnt = [0]*10
for i in list_num:
    cnt[i] += 1

for i in cnt:
    print(i)




