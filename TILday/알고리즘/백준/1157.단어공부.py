str = list(input().upper())
word = list(set(str)) #set은 순서가 없다
# print(set_str)
cnt = []

for i in word:
    count = str.count(i)
    cnt.append(count)
# print(cnt)
# max_cnt = []
# for i in cnt:
#     if i > i+1:
#         max_cnt.append(i)
#         if max_cnt == i:
#             max_cnt.append(i)
#
# print(max_cnt)


if cnt.count(max(cnt)) >=2:
    print('?')
else:
    print(word[(cnt.index(max(cnt)))])



