n = int(input())


start = 1
temp = 0

while True:
    if n == start:
        print(temp + start)
        break

    elif start < n:
        n -= start
        start += 1

    elif start > n:
         temp += start - 1
         start = 1



