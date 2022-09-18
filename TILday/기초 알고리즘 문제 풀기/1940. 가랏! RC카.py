T = int(input())
for tc in range(1, T+1):
    N = int(input())
    
    sec = 0
    speed = 0

    for i in range(N):
        value = input().split()
        if value[0] == '0' :
            v = v
            length += v
        elif value[0] == '1' :
            v += int(value[1])
            length += v
        else :
            if int(value[1]) > v :
                v = 0
                length = length
            else :
                v -= int(value[1])
                length += v
