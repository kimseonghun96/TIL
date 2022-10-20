
#2050. 알파벳을 숫자로 변환
T = list(input())               #리스트로 받을 변수 만듬
for i in range(len(T)):         #for문을 이용해 함수의 길이만큼 반복
	print(ord(T[i])-64, end="") # ord()는 알파벳을 숫자로 바꿔줌 A가 65이므로 64를 빼준다, 나온 값 뒤에 띄우기 위해 end=" " 사용

#2047. 신문 헤드라인 D1
str_small = str(input())   #소문자로 된 문자를 받을 변수 만듬
print(str_small.upper())   #소문자를 대문자로 바꾸는 upper()사용


# 2056. 연월일 달력
# T = int(input()) #테스트 케이스 숫자

# year_num = int(input())
# year = year_num[:4]
# mount = year_num[5::7]
# day = year_num[7:]

# for i in year:
#     year = i
#     print(year)
#     pass
    
#     for j in mount:
#         if j <= 12:
#             print(j)
#         else:
#             print(-1)
#             break
        
#         for k  in day:
#             if k < 32:
#                 print(k)
#             if j == 2 and k > 28:
#                 print(-1)
#                 break
#     print(f'# {year}/{j}/{k}')


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
for test_case in range(1, T + 1):
   case = str(input())
   year = case[0:4]
   month = case[4:6]
   day = case[6:8]
   
   answer = ''
   if 0 < int(month) < 13 and 0 < int(day) <= days[int(month)]:
       answer = year + '/' + month + '/' + day
   else:
       answer += '-1'

   print("#" + str(test_case) + " " + answer)