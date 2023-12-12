n, s, r = map(int, input().split())
damaged_ca = list(map(int, input().split()))
extra_ca = list(map(int, input().split()))

result = 0
for team in damaged_ca:
    if team - 1 in extra_ca:
        extra_ca.remove(team - 1)
    elif team + 1 in extra_ca:
        extra_ca.remove(team + 1)
    else:
        result += 1


print(result)
