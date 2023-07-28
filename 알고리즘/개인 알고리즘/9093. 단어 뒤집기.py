# 단어마다 뒤집어야하는데
# 한 번 문장 자체를 뒤집고 뒤부터 출력하면 되잖아


T = int(input())

for tc in range(T):
    words = input().split()

    ans = []

    for i in range(len(words)):
        ans.append(words[i][::-1])

    print(' '.join(ans))