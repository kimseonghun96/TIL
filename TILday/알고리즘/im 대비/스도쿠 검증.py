# 가로, 세로,  박스의 길이가 다르면 0 같으면 1
'''
1
7 3 6 4 2 9 5 8 1
5 8 9 1 6 7 3 2 4
2 1 4 5 8 3 6 9 7
8 4 7 9 3 6 1 5 2
1 5 3 8 4 2 9 7 6
9 6 2 7 5 1 8 4 3
4 2 1 3 9 8 7 6 5
3 9 5 6 7 4 2 1 8
6 7 8 2 1 5 4 3 9
'''


# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# T = 10
# for tc in range(1, T+1):
#     arr = [list(map(int, input().split())) for _ in range(9)]
#     for r in range(9):
#         for c in range(9):
#             r_list = set()
#             c_list = set()
#             box_list = set()
#             for k in range(4):
#                 if 0 <= r < 9 and 0 <= c < 9:
#                     nr = r + dr[k]
#                     nc = c + dc[k]
#                     r_list.add(arr[nr][c])
#                     c_list.add(arr[r][nc])
#
#             for t in range(3):
#                 for z in range(3):
#                     box_list.add(arr[t][z])
#
#             if len(r_list) == len(c_list) == len(box_list):
#                 print(1)
#             else:
#                 print(0)


'''
1
7 3 6 4 2 9 5 8 1
5 8 9 1 6 7 3 2 4
2 1 4 5 8 3 6 9 7
8 4 7 9 3 6 1 5 2
1 5 3 8 4 2 9 7 6
9 6 2 7 5 1 8 4 3
4 2 1 3 9 8 7 6 5
3 9 5 6 7 4 2 1 8
6 7 8 2 1 5 4 3 9
'''


# r, c, box를 set으로 만들어서
# for문을 돌면서 하나씩 담을 것
# 스도쿠가 맞다면 겹치는 번호가 없을 것이므로 길이를 비교해서
# 같다면 1 틀리면 0을 출력하려 했음

# T = int(input())
# for tc in range(1, T+1):
#     arr = [list(map(int, input().split())) for _ in range(9)]
#     doku = 9
#     # r_list = set()
#     # c_list = set()
#     # box_list = set()
#     ans = 1
#
#     for r in range(9):
#         temp = set()
#         for c in range(9):
#             temp.add(arr[r][c])
#         if len(temp) != doku:
#             ans = 0
#
#     for x in range(9):
#         temp = set()
#         for y in range(9):
#             temp.add(arr[y][x])
#         if len(temp) != doku:
#             ans = 0
#
#     for t in range(3):
#         for z in range(3):
#             temp = set()
#             for q in range(t*3, t*3+3):
#                 for w in range(z*3, z*3+3):
#                     temp.add(arr[q][w])
#             if len(temp) != doku:
#                 ans = 0
#
#     print(f'#{tc} {ans}')

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    doku = 9
    ans = 1

    for r in range(9):
        r_list = set()
        c_list = set()
        for c in range(9):
            r_list.add(arr[r][c])
            c_list.add(arr[c][r])
        if doku != len(r_list) or doku != len(c_list):
            ans = 0

    for t in range(3):
        for z in range(3):
            box_list = set()
            for q in range(t*3, t*3+3):
                for w in range(z*3, z*3+3):
                    box_list.add(arr[q][w])
            if len(box_list) != doku:
                ans = 0

    print(f'#{tc} {ans}')




