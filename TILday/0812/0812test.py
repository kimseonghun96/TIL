'''
문자를 입력받고 제거할 문자를 리스트로 만들어야되나?
'''

word = input()                        # 문자 받음
remove_word = list('CAMBRIDGE')       # 제거할 문자 리스트로 만듬
new_word = ''                         # 새로운 문자열 받을 곳 만듬
for i in word:                        # word를 돌면서
    if not i in remove_word:          # 겹치는 것이 없는 i를
        new_word += i                 # new_word에 추가시킴

print(new_word)





