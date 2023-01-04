N = int(input())


temp = []
for i in range(N):
    word = input()
    temp.append(word)

set_word = list(set(temp))

sort_word = []
for i in set_word:
    sort_word.append((len(i), i))

# print(sort_word)

ans = sorted(sort_word)

for len_word, word in ans:
    print(word)
