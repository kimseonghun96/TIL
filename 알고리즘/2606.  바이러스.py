computer = int(input())

n = int(input())
ans = []

for i in range(n):
    a, b = map(int, input().split())
    if i == 0:
        ans.append(a)
        ans.append(b)


    else:
        if a or b in ans:
            ans.append(a)
            ans.append(b)
        else:
            pass



# set(ans)

print(ans)

