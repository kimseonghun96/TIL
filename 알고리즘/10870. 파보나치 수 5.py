n = int(input())

ans =[0, 1]

num = 20

while num:
    ans.append(ans[-1] + ans[-2])
    num -= 1

print(ans[n])

## 파보나치

