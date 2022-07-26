url = 'http://naver.com'
my_str = url.replace('http://', '') # my_str문장에서 'http://를 ''(빈칸)으로 바꿔줘
print(my_str)
my_str = my_str[:my_str.index('.')] # my_str 문장에서 . 앞까지 짤라줘 = my_str[0:5]
print(my_str)

password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + '!'
    # my_str 3번째 앞자리 까지 짜르고 + my_str의 개수 + e의 개수(count 매서드 사용)  # 정수여서 문자열로 바꾸는 str 사용 

print('{0}의 비밀번호는 {1}입니다.'.format(url, password))

#리스트 [] 순서를 가진 객체의 집합

subway = ['유재석', '조세호', '박명수']

#조세호가 몇번째에 타있는가?
print(subway.index('조세호'))

#하하가 다음 정류장에서 탐 추가
subway.append('하하')
print(subway)

#정형돈을 유재석 조세호 사이에 추가
subway.insert(1, '정형돈') #어디에 넣을 것인지 인덱스부터 적는다.
print(subway)

#뒤에서 부터 한명식 꺼냄
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

#유재석이 몇명인지 확인
subway.append('유재석')
print('유재석')
print(subway.count('유재석'))

#정렬도 가능
num_list = [5, 2, 4, 3, 1]
num_list.sort() #정렬
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

#모두지우고 틀만 남기는건 clear
#리스트 확장
mix_list = ('조세호', 20 , True)
num_list.extend(mix_list) #extend() ()안의 리스트를 합친다.
print(num_list)