''' 조건문
a = 5
if a > 5:
    print('5 초과')
else:
    print('5 이하')
'''

'''
num = int(input()) # int를 붙이지 않으면 문자열 그대로 되기 때문에 int를 붙여 숫자로 만듬
if num % 2 == 1:
    print('홀수')
else:
    print('짝수')
'''

''' 복수조건문
dust = 80
if dust > 150:
    print('매우 나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:                           # 위의 모든 조건이 False인 경우
    print('좋음')
print('미세먼지 확인 완료')
'''


''' 중첩 조건문
dust = 500
if dust > 150:
    print('매우 나쁨')
    if dust > 300:                  #추가된 내용
        print('실내 활동을 자제하세요.')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
elif dust >= 0:
    print('좋음')
else:             # 위의 모든 조건이 False인 경우
    print('값이 잘못 되었습니다')
'''

# 조건 표현식 true인 경우 = 값 if 조건 else false인 경우 값 (조건이 중간에 들어감)

'''
num이 정수일 때, 절댓값을 저장하기 위한 코드
vlaue = num if num >= 0else -num
'''

''' if문을 조건 표현식으로 바꾼 것
num = 2
if num % 2 :
    result = '홀수입니다.'
else:
    result = '짝수입니다'
print(result)

num = 2
result = '홀수입니다.' if num % 2 else '짝수입니다.'
print(result)
'''

#반복문 특정 조건을 만족할 때까지 같은 동작을 계속 반복하고 싶을 때 사용
# while 문 - 종료 조건에 해당하는 코드를 통해 반복문을 종료시켜야 함
# for 문 - 반복가능한 객체를 모두 순회하면 종료(별도의 종료 조건이 필요 없음) ex) 횟수 반복, 별 찍기
# 반복 제어 - break, contiune, for-else - 특정 상황에서 반복문을 멈출 때

'''
while 문 : 조건이 참인 경우 반복적으로 코드를 실행
- 조건이 참인 경우 들여쓰기 되어 있는 코드 블록이 실행됨
- 코드 블록이 모두 실행됙, 다시 조건식을 검사하며 반복적으로 실행됨
- while문은 무한 루프를 하지 않도록 종료 조건이 반드시 필요 

a = 0
while a< 5: #종료조건
    print(a)
    a += 1 #반복시 a가 계속 증가
print('끝')

#복합연산자 - 연산과 할당을 합쳐놓은것

cnt = 100
cnt += 1 #cnt = cnt + 1

cnt = 0
while cnt < 3:
    print(cnt)
    cnt += 1
'''

#for문은 시퀀스(string, tuple, list, range)를 포함한 순회 가능한 객치(literable)의 요소를 모두 순회
# - 처음부터 끝까지 모두 순회하므로 별도의 종료 조건이 필요하지 않음
#literable - 순회할 수 있는 자료형(string, list, tuple, range, set 등), 순회형 함수(range, enumerate)

'''
for fruit in ['apple', 'mango', 'banana']:
    print(fruit)
print('끝')

#for문을 이용한 문자열(string)순회
chars = input()
for char in chars:
    print(char)

chars = input()
for idx in range(len(chars)):
    print(chars[idx])
'''

'''
#딕셔너리 순회 - 딕셔너리는 기본적으로 key를 순회하며, key를 통해 값을 활용
grades = {'join' : 80, 'eric' : 90}
for student in grades:
    print(student)

grades = {'join' : 80, 'eric' : 90}
for student in grades:
    print(student, grades[student])

#추가 메서드를 활용하여 순회할 수 있음
# key() : key로 구성된 결과
#vlaues() : value로 구성된 결과
#items() : (Key, value)의 튜플로 구성된 결과
grades = {'jhon' : 80, 'eric' : 90}
print(grandes.keys())
print(grandes.vlaues())
print(grandes.items())
#자주 쓰는 items
grades = {'jhon' : 80, 'eric' : 90}
for student, grade in grades.items():
    print(student, grade)
'''
'''
#enumerate() - 인덱스와 객체를 쌍으로 담은 열거형(enumerate) 객체 변환
#(index, value) 형태의 tuple로 구성된 열거 객체를 변환
members = ['민수', '영희', '철수']
for idx, number in enumerate(members):
    print(idx,number)

members = ['민수', '영희', '철수']
enumerate(members)
print(list(enumerate(members)))
print(list(enumerate(members, start =1))) #start =1 기본값 0, start를 지정하면 해당 값부터 순차적으로 증가.
'''

#List comprehension - 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법!! 진짜 많이쓰임!
# 문법 [code for 변수 in iterable], [code for 변수 in iterable if 조건식]
'''
cubic_list = [] #1~3의 세제곱 리스트 만들기
for number in range(1,4):
    cubic_list.append(number ** 3)
print(cubic_list)

cubic_list = [number ** 3 for number in range (1, 4)]
print(cubic_list)
'''

'''
#Dictionary Comprehension - 표현식과 제어문을 통해 특정한 값을 가진 딕셔너리를 간결하게 생성하는 방법
#문법 {key : value for 변수 in iterable}, {key : value for 변수 in iterable if 조건식}
cubic_dict = {}  #1~3의 세제곱 딕셔너리 만들기
for number in range(1, 4):
    cubic_dict[number] = number ** 3
print(cubic_dict)

cubic_dict ={number : number ** 3 for number in range(1, 4)}
print(cubic_dict)
'''

'''
반복문 제어
- break : 반복문을 종료 (중간에 멈추는 느낌)
n = 0
while True:
    if n == 3:
        break
    print(n)
    n += 1   # 0, 1, 2 (3에서 종료되니까)

for i in range(10):
    if i > 1:
        print('0과 1만 필요해!') # 0,1 '0과 1만 필요해!'(2를 만나서)
        break #종료
    print(i) #실행x
- continue : contine 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행(건너뛰기)
- for-else : 끝까지 반복문을 실행한 이후에 else문 실행, 주의할점 : break를 통해 중간에 종료되는 경우 else 문은 실행되지 않음
- pass : 아무것도 하지 않음(문법적으로 필요하지만, 할 일이 없을 때 사용) 
'''

#continue - continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행
'''
for i in range(6):
    if i % 2 == 0:
        continue
    print(i)
'''

#Pass - 아무것도 하지않음, 특별히 할 일이 없을 때 자리를 채우는 용도로 사용, 반복문 아니어도 사용 가능
#i가 2일때 pass
'''
for i in range(4):
    if i ==2:
        pass
    print(i)
'''

#i가 2일때 continue()
'''
for i in range(4):
    if i = =2 :
        continue
    print(i)
'''    
#else - 끝까지 반복문을 실행한 이후에 else문 실행
'''
for char in 'apple':
    if char == 'b'
    print('b!')
    break
else:
    print('b가 없습니다.') #b가 없습니다.

for char in 'banana':
    if char == 'b'
    print('b!')
    break
else:
    print('b가 없습니다.') #b!
    '''

# 함수!! - Decomposition(분해), Abstraction(추상화)
# Decomposition(분해)

#평균 구하는 코드
'''
numbers = [1, 2, 3] 
print(sum(numbers) / len(numbers))

number = [1, 2, 3]
def average(numbers):
    return sum(numbers) / len(numbers)

print(average(numbers))
'''
#Abstraction(추상화) - 복잡한 내용을 모르더라도 사용할 수 있도록(스마트폰) 재사용성과 가독성, 생산성
#사실 내부 구조를 변경할게 아니라면 몰라도 무방, 그것이 함수의 장점이자 프로그래밍의 매령, 스마트폰의 원리를 잘 몰라도 우리는 잘 사용할 수 있음

#주의 - print 함수와 return의 차이점
# print를 사용하면 호출될 때마다 값이 출력됨(주로 테스트를 위해 사용)
# 데이터 처리를 위해서는 return 사용

# return은 항상 하나의 값만 반환한다. 두개 이상의 값을 반환하는 방법은?
'''
반환 값을 튜플로 사용
def minus_and_product(x, y):
    return x - y, x * y
y = minus_and_product(4, 5)
print(y)
print(type(y))
'''
#함수 반환 정리
#return x -> none(void)
#return o -> 하나를 반환 ,  여러개를 원하면, Tuple활용
#똑바로 읽어도 거꾸로 읽어도 같은 단어를 찾는 함수
'''
word_list = ['우영우', '기러기', '별똥별', '파이썬']
def is_palindrome(word_list):
    palindrome_list = []
    for word in word_list:
        if word == word[::-1]:
          palindrome_list.append(word)
        return palindrome_list
print(is_palindrome(word_list))
'''

# 함수의 입력
# parameter : 함수를 정의할 때, 함수 내부에서 사용되는 변수
# Argument : 함수를 호출 할 때, 넣어주는 값
'''
def function(hma): #parameter : ham
    return ham

function('spam') #argument : 'spam'
'''

#가변 인자(*args)와 가변 키워드 인자 (**kwargs) 동시 사용 예시
#가변 인자와 가변 키워드 인자를 함께 사용할 수 있음
'''
def print_family_name(*parents, **pets):
    print("아버지 :", parents[0])
    print("어머니 :", parents[1])
    if pets:
        print("반려동물들..")
        for title, name in pets.items():
            print('{} : {}'.format(title, name))

print_family_name('아부지', '어무이', dog = '멍멍이', cat = '냥냥이' )
'''

#python의 범위(Scope)
'''
-함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분
-scope
  global scope : 코드 어디에서든 참조할 수 있는 공간
  local scope : 함수가 만든 scope. 함수 내부에서만 참조가능
-variable
  global variable : global scope에 정의된 변수
  local variable : local scope에 정의된 변수
'''

#변수 수명주기(lifecycle)