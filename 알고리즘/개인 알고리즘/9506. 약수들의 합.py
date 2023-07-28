# 일단 약수 구하고
# 자신을 제외면 마지막에 오는 수 빼고 더한게
# 자신과 같으면 ㅇㅋ

while True:
    n = int(input())
    if n == -1:
        break

    temp = []

    for i in range(1, 100001):
        if i >= n:
            break
        else:
            if n % i == 0:
                temp.append(i)

    if n == sum(temp):
        print(f'{n} =', ' + '.join(str(i) for i in temp))
    else:
        print(f'{n} is NOT perfect.')

