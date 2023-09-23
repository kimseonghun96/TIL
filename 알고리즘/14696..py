round = int(input())
for i in range(round) :
    A = list(map(int,input().split()))[1:]
    B = list(map(int,input().split()))[1:]
    listA = [A.count(4),A.count(3),A.count(2),A.count(1)]
    listB = [B.count(4),B.count(3),B.count(2),B.count(1)]
    if listA[0] > listB[0] :
        print('A')
    elif listA[0] < listB[0] :
        print('B')
    elif listA[1] > listB[1] :
        print('A')
    elif listB[1] > listA[1] :
        print('B')
    elif listA[2] > listB[2] :
        print('A')
    elif listB[2] > listA[2] :
        print('B')
    elif listA[3] > listB[3] :
        print('A')
    elif listB[3] > listA[3] :
        print('B')
    else :
        print('D')