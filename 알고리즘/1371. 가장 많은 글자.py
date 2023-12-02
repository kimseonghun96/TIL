# sys.stdin.readline() -> 여러 문자를 입력 받기 위해
# ord(), chr() 아스키 코드로 변환하는 거





import sys

input = sys.stdin.read

strarr = input().replace("\n","").replace(" ","")

word = [0 for i in range(26)]


for s in strarr:
    if s.islower():
        word[ord(s) - 97] += 1      # 알파벳을 아스키코드로 변환

for i in range(26):
    if word[i] == max(word):
        print(chr(i + 97), end = "")  # 아스키코드에 해당되는 문자로 반환