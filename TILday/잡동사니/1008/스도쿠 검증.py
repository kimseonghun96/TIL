T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    N = 9
    ans = 1

    r_list = []
    c_lsit = []
    for r in range(N):
        temp = set()
        temp2 = set()
        for c in range(N):
            temp.add(arr[r][c])
            temp2.add(arr[c][r])
        temp = list(temp)
        temp2 = list(temp2)
        r_list.append(temp)
        c_lsit.append(temp2)
    # print(r_list)
    # print(c_lsit)
    box = []
    for r in range(3):
        for c in range(3):
            temp3 = set()
            for x in range(r*3, 3 + (r*3)):
                for y in range(c*3, 3+(c*3)):
                    temp3.add(arr[x][y])
            temp3 = list(temp3)
            box.append(temp3)
    r_list.sort()
    c_lsit.sort()
    box.sort()

    # print(r_list)
    # print(c_lsit)
    # print(box)

    for k in range(N):
        if len(r_list[k]) != len(c_lsit[k]) or len(r_list) != len(box[k]) or len(c_lsit) != len(box):
            ans = 0


    print(f'#{tc} {ans}')



