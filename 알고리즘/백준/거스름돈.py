n = int(input())

result = 1000 - n
count = 0

array = [500, 100, 50, 10, 5, 1]

for coin in array:
    count += result//coin
    result %= coin

print(count)