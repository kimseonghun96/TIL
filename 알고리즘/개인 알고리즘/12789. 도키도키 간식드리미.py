import sys

input = sys.stdin.readline

N = int(input())
people = list(map(int, input().split()))

check_num = []
new_line = [0]

for i in range(1, N + 1):
    check_num.append(i)

for j in range(10000):
    if len(people) == 0:
        break
    if check_num[0] != people[0] and check_num[0] != new_line[-1]:
        new_line.append(people[0])
        people.pop(0)

    elif check_num[0] == people[0] :
        check_num.pop(0)
        people.pop(0)
    elif check_num[0] == new_line[-1]:
        check_num.pop(0)
        new_line.pop()

    # print('people : ', people)
    # print('new_line: ', new_line)
    # print('check_num: ', check_num)
    # print('--------------------------')
for i in range(len(check_num)):
    if check_num[0] == new_line[-1]:
        check_num.pop(0)
        new_line.pop(-1)


if len(check_num) == 0:
    print('Nice')
else:
    print('Sad')