'''
5
123123
124467
333444
444456
123444
'''

# # 1
# def f(i, k):
#     global ans
#     if i == k:
#         run = 0
#         tri = 0
#         if card[0] == card[1] and card[1]==card[2]:
#             tri += 1
#         if card[0]+1 == card[1] and card[1]+1 == card[2]:
#             run +=1
#         if card[3] == card[4] and card[4]==card[5]:
#             tri += 1
#         if card[3]+1 == card[4] and card[4]+1 == card[5]:
#             run +=1
#         if tri + run == 2:
#             ans = 'babjin'
#
#     else:
#         for j in range(i, k):
#             card[i], card[j] = card[j], card[i]
#             f(i+1, k)
#             card[i], card[j] = card[j], card[i]
#
#
# T = int(input())
# for tc in range(1, T+1):
#     card = list(map(int, input()))
#     ans = 'Lose'
#     f(0, 6)
#     print(f'#{tc} {ans}')

# print('*-------------------------------------------------')

#2
# def f(i, k):
#     if i == k:
#         run = 0
#         tri = 0
#         if card[0] == card[1] and card[1]==card[2]:
#             tri += 1
#         if card[0]+1 == card[1] and card[1]+1 == card[2]:
#             run +=1
#         if card[3] == card[4] and card[4]==card[5]:
#             tri += 1
#         if card[3]+1 == card[4] and card[4]+1 == card[5]:
#             run +=1
#         if tri + run == 2:
#             return  1
#         else:
#             return  0
#
#     else:
#         for j in range(i, k):
#             card[i], card[j] = card[j], card[i]
#             if f(i+1, k):
#                 return 1
#             card[i], card[j] = card[j], card[i]
#         return 0
#
# T = int(input())
# for tc in range(1, T+1):
#     card = list(map(int, input()))
#
#     ans = f(0, 6)
#     if ans:
#         print(f"#{tc} BabyGin")
#     else:
#         print(f"#{tc} Lose")


# print('*-------------------------------------------------')


#3
T = int(input())
for tc in range(1, T+1):
    card = int(input())
    c = [0]* 12

    i = 0
    while i < 6:
        c[card%10] +=1
        card//= 10
        i += 1

    tri = 0
    run = 0
    i = 0
    while i < 10:
        if c[i] >= 3:
            c[i] -= 3
            tri += 1
            continue
        if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            run += 1
            continue
        i += 1

    if run+tri == 2:
        print(f'#{tc} Babyjin')
    else:
        print(f'#{tc} Lose')



