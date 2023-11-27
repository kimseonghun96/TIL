# 8진수로 이미 되어 있기 때문에
# 8진수 한개씩 끊어 2진수로 만들기


n = input()
result = []
ans = ''
for num in n:
    for _ in range(3):    # 8 진수는 0~7 3자리.
        # 각자리수를 이진변환
        result.append(str(int(num) % 2))
        num = int(num) // 2
    # print(result) # ['1', '1', '0']
    result = result[::-1]
    # print(result) #['0', '1', '1']
    ans += ''.join(result)
    result = []

print(int(ans))
#11001100

print(bin(int(input(), 8))[2:])
#11001100