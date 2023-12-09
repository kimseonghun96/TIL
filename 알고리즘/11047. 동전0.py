# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

n, k = map(int, input().split())
ans = 0
arr = []




for i in range(n):
    num = int(input())
    arr.append(num)

# coins.sort(reverse=True) 뒤집는 거
for i in arr[::-1]:
    if k >= i:
        ans += k // i
        k = k % i

print(ans)
