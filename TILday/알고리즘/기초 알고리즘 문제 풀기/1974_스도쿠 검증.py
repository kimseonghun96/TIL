import sys
sys.stdin = open('input2.txt')

T = int(input())
for tc in range(1, T+1):
    N = 9
    arr = [list(map(int, input().split())) for _ in range(9)]
    # box = [[]*3 for _ in range(3)]     # 굳이? 만들어야되나
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # print(arr)
    # print(box)

    row_list = []
    for r in range(9):                              #가로를 하나씩 출력해야된느데
        temp_list = []
        for c in range(9):
            temp_list.append(arr[r][c])
        # print(temp_list)
        row_list.append(list(set(temp_list)))

    # print(row_list)

    col_list = []
    for r in range(9):
        temp_list = []
        for c in range(9):
            temp_list.append(arr[c][r])
        col_list.append(list(set(temp_list)))

    box_list = []
    for r in range(3):
        for c in range(3):
            temp_list = []
            for i in range(r*3, (r*3)+3):
                for j in range(c*3, (c*3)+3):
                    temp_list.append(arr[i][j])
            # print(box_list)
            box_list.append(list(set(temp_list)))
            # print(box_list)
            # if arr[r][c] != arr[r+1][c] or arr[r][c] != [r][c+1]:
            # box_list.append(list(arr[r][c]))
            # box_list.append(list(arr[c][r]))
            #         print(box_list)
    # else:
    #     continue
    #     # print(num_box)
    for i in range(9):
        if len(num) != len(row_list[i]) or len(num) != len(col_list[i]) or len(num) != len(box_list[i]):
            print(f'#{tc} 0')
            break
    else:
        print(f'#{tc} 1')


print('-----------------------------------------------------------------------------------')
import sys
sys.stdin = open('test_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = 9               # N*N
    arr = [list(map(int, input().split())) for _ in range(9)]  # 리스트 받음
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    row_list = []           # 하나씩 담기위해 초기화되면 안되서
    for r in range(9):
        temp_list = []
        for c in range(9):
            temp_list.append(arr[r][c])
        row_list.append(list(set(temp_list)))

    col_list = []
    for r in range(9):
        temp_list = []
        for c in range(9):
            temp_list.append(arr[c][r])
        col_list.append(list(set(temp_list)))

    box_list = []
    for r in range(3):                              # 3번 돌꺼
        for c in range(3):
            temp_list = []
            for i in range(r*3, (r*3)+3):           # 위의 r,c와 연결되야해서 r,c 넣고 맞춰야됨
                for j in range(c*3, (c*3)+3):
                    temp_list.append(arr[i][j])
            box_list.append(list(set(temp_list)))

    for i in range(9):          # 9번 봐야되기 때문
        if len(num) != len(row_list[i]) or len(num) != len(col_list[i]) or len(num) != len(box_list[i]):
            print(f'#{tc} 0')
            break               # break 안걸면 많이 반복됨
    else:
        print(f'#{tc} 1')





