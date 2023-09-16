import sys

input = sys.stdin.readline

words = [list(input().strip()) for _ in range(5)] # strip() -> '/n' 개행 없애줌

max_len_word = max(len(word) for word in words)

for i in range(5):
    if len(words[i]) < max_len_word:
        words[i].extend([''] * (max_len_word - len(words[i]))) # append는 단일 extend는 다수 가능

zipped_words = list(zip(*words))

for i in zipped_words:
    print(''.join(i), end='')
