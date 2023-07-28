# 대문자, 소문자 리스트를 만들고
# 문자열이 들어왔을 때 비교해서 그 값이 있다면
# 그 값을 check 하고 문자 리스트에서 찾아서
# 13번째 뒤에 있는 거랑 바꿔주면 될 듯?

sentence = list(map(str, input()))

big = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
small = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in range(len(sentence)):
    if sentence[i] in big:
        check = (big.index(sentence[i]) + 13) % 26
        sentence[i] = big[check]
    elif sentence[i] in small:
        check = (small.index(sentence[i]) + 13) % 26
        sentence[i] = small[check]

print(''.join(sentence))




