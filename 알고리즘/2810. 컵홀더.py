N = int(input())
seat = input()

cupholders = 1

i = 0
while i < N:
    if seat[i] == 'S':
        cupholders += 1
        i += 1
    else:
        cupholders += 1
        i += 2

# 컵홀더의 수와 좌석의 수 중 작은 값을 선택하여 출력
print(min(cupholders, N))
