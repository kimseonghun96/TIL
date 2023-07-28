x, y = map(int, input().split())

month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

ans = 0
for i in range(1, len(month_day)+1):
    if i == x:
        ans = (sum(month_day[:x-1]) + y) % 7

print(day[ans])

