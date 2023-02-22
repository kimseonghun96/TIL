# 1. 거스름돈: 가장 큰 화폐부터 거슬러 주면 된다.
n = int(input())

result = 1000 - n
count = 0

array = [500, 100, 50, 10, 5, 1]

for coin in array:
    count += result//coin
    result %= coin

print(count)

# 2. 1이 될 때까지: 주어진 N에 대하여 최대한 많이 나누기를 수행
n, k = map(int, input().split())

result = 0

while True:
    # n이 k로 나누어 떨어지는 수가 될 때 가지 빼기
    target = (n // k) * k
    result += (n-target)
    n = target
    # n이 k보다 적을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # k로 나누기
    result += 1
    n //= k

# 3. 곱하기 혹은 더하기 : 두 수에 대하여 연산을 수행할 때, 두 수 중에서 하나라도 1 이하인 경우에는 더하며, 두 수가 모두 2이상인 경우에는 곱하면 된다.
data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)


# 4. 모험가 길드 : 오름차순 정렬 이후에 공포도가 가장 낮은 모험가부터 확인.
'''
5
2 3 1 2 2
'''
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹의 수
conut = 0   # 현재 그룹에 포험된 모함가의 수

for i in data:  # 공포도를 낮은 것부터 하나씩 확인하며
    conut += 1  # 현재 그룹에 해당 모험가를 포함시키기
    if conut >= i:  # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1 # 총 그룹의 수 증가시키기
        conut = 0   # 현재 그룹에 포함된 모험가의 수 초기화

print(result)   # 총 그룹의 수 출력