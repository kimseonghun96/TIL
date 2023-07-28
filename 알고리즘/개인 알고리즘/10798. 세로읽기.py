# 2차원 리스트를 만들고
# 가장 긴 리스트의 길이를 찾은 다음
# 작은 리스트에 ['']를 추가해서 길이를 맞춰 준 후
# 이걸 zip으로 묶어내면 될 거 같은데

words = []

for _ in range(5):
    words.append(list(input()))

max_len = max(len(word) for word in words)

for i in range(5):
    if len(words[i]) < max_len:
        words[i].extend([''] * (max_len - len(words[i])))

zipped_words = list(zip(*words))

for row in zipped_words:
    print(''.join(row), end='')



