'''
5
abcdefghijklmnopqrstu
abcdefghijklmnopqrstuvwzyx
abcefghijk
xyz
absolute
'''

# 영어 알파벳이 순서대로 정렬된 리스트를 만들고
# 정렬된 알파벳과 인풋의 알파벳의 인덱스가 같으면 +1
# 다를 경우 멈추고 출력

list_word = list('abcdefghijklmnopqrstuvwxyz')

T = int(input())
for tc in range(1, T+1):
    string = list(input())
    ans = 0
    for i in range(len(string)):
        if string[i] == list_word[i]:
            ans += 1
        else:
            break
    print(f'#{tc} {ans}')