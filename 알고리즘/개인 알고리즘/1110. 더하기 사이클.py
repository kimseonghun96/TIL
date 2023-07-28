# 일단 두자리 숫자이기 때문에 이걸 쪼개
# 10보다 작을 경우 앞에 0을 붙여서 두자리로 만든 후
# 처음과 같은 숫자가 되면 멈춤
# 사이클당 한 번 씩 더해야 됨

N = int(input())

num = N

cnt = 0
while True:
    sum_num = num // 10 + num % 10
    new_num = (num % 10) * 10 + sum_num % 10
    cnt += 1
    if new_num == N:
        break
    num = new_num

print(cnt)
