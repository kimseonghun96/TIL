n, m = map(int, input().split())
cards = list(map(int, input().split()))


ans = 0

for i in cards:
    for j in cards:
        for k in cards:
            if i != j and j != k and k !=i:
                if ans < i + k + j <= m:
                    ans =  i + k + j

print(ans)