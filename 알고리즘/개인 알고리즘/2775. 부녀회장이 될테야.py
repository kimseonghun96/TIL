T = int(input())

for i in range(T):
    ans = 0
    floor = int(input())
    room_num = int(input())
    floor0 = [j for j in range(1, room_num+1)]
    for k in range(floor):
        for t in range(1, room_num):
            floor0[t] += floor0[t-1]
    print(floor0[-1])


