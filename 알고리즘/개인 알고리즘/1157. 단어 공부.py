str = list(input().upper())
word = list(set(str))
# print(word)
cnt = []

for i in word:
    check = str.count(i)
    # print(check)
    cnt.append(check)

if cnt.count(max(cnt)) >=2:
    print('?')
else:
    print(word[(cnt.index(max(cnt)))])