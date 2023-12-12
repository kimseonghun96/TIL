txt = input()
search = input()
cnt = 0
length_search = len(search)

i = 0

while i <= len(txt) - length_search:  # 범위를 벗어나지 않도록 수정
    if txt[i:i+length_search] == search:
        cnt += 1
        i += length_search  # 찾은 패턴 이후로 인덱스 이동
    else:
        i += 1

print(cnt)
