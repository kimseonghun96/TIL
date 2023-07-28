N = int(input())

ans = 0
if (N % 5) % 3 == 0:
    ans = (N//5) + (N % 5)//3


elif (N % 5) % 3 != 0:
    if N % 3 == 0:
        ans = N//3

    elif N % 3 != 0:
        if (N % 8) == 3 or (N % 8) == 5:
            ans = 2*(N//8) + 1

    else:
        ans = -1

print(ans)