fibonacci = []
for i in range(41):
    if i == 0:
        fibonacci.append(0)
    elif i == 1:
        fibonacci.append(1)
    else:
        fibonacci.append(fibonacci[i - 2] + fibonacci[i - 1])

T = int(input())
results = []

for tc in range(T):
    n = int(input())
    if n == 0:
        results.append([1, 0])
    elif n == 1:
        results.append([0, 1])
    else:
        results.append([fibonacci[n - 1], fibonacci[n]])

for result in results:
    print(result[0], result[1])