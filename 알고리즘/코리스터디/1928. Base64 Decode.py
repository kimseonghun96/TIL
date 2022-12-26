# 받은 문자열을 6씩 나누고
# 문자 조건 숫자 조건을 만든 후
# 아스키 코드로 변환
# ord() = 문자 -> 아스키 코드, chr() = 아스키 코드 -> 문자


T = int(input())
for tc in range(1, T+1):
    string = list(input())
    temp = []
    for i in range(1, len(string)+1):
        if i % 6 == 0:
            for k in range(i):
                temp.append(string[k])
    print(temp)
