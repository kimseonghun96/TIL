word = 'abcdefghijklmnopqrstuvwxyz'
S = input()
for i in word:
    print(S.find(i), end = ' ')
    #find()함수는 위치를 바로 반환한다.