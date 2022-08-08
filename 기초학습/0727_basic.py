# 딕셔너리
cabinet = {3 : '유재석', 100 : '김태호'}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3)) # get 쓸 땐 소괄호
print(cabinet.get(5))# 딕셔너리 안에 없어도 넌 발생하고 계속됨
# print(cabinet[5]) # 딕셔너리 안에 없어서 오류발생 종료

print(3 in cabinet) # 3이라는 변수가 캐비넷에 있으면 True, 없으면 Flase

 