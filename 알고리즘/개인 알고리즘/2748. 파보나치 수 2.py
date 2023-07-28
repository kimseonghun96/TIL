# 0, 1 시작하는 값을 먼저 적고
# 계속 더한것을 리스트에 추가하면서
# 인덱스 n의 값을 추출?

n = int(input())

fa_list = [0, 1]

while True:
    if n == len(fa_list) - 1:
        break
    fa_list.append(fa_list[-1] + fa_list[-2])

print(fa_list[-1])

