# Gravity
'''
인풋의 첫번째 줄에는 테스트케이스의 개수 T가 주어진다.
각 테스트케이스는 첫번째 줄에 방의 크기 N이 주어짐
그 다음줄에는 각 열에 쌓인 상자들의 높이가 띄어쓰기로 구분되어 주어짐

인풋은 모양을 나타내는 것

숫자는 상자의 높이를 나타낸다.

어떻게 풀것인가? -> 어떻게 저장할 것인가?
그림부터 그려봐야된다.

평명형태 : 2차원
상자들의 꼭대기만 알면 문제를 풀 수 있다.
(높이만 알면 된다.)
아래쪽에 있는 상자들은 꼭대기에 있는 상자들보다
낙차가 클 수 없다.

회전을 했을때 비어있는 칸만큼 떨어 질 것이다.
나보다 작은 것이 몇개가 있느냐 파악해야됨
대소비교, 숫자형태로 순서대로 저장해야됨
한줄 단위로 받아간다.
'''
#테스트 케이스 개수 입력
#input() : 가로 한 줄 문자열 형태로 입력받기
# T =  int(input) # 개수니까 숫자로 변경

# N = int(input())
# boxes = list(map(int, input().split())) #맵에 int 적으면 모든 요소를 숫자로 바꾸겠다라는 뜻 + list로 다시감싼다.

# # 각 상자열의 꼭대기에 있는 높이 구하기
# # 0번 열의 꼭대기 상자가 떨어지는 낙차구하기: 1번~N-1번까지 상자열중에 0번열 보다 높이가 작은 개수를 구하면됨
# #0번열의 높이 vs 1번~N-1번 열의 높이 비교
# result = 0
# for i in range(0, N-1):
# cnt = 0 # 카운트 변수
#     for j in range(i+1,N):
#         boxes[i] > boxes[j]:
#             cnt += 1
#     if result < cnt:
#         result = cnt
# print(result)
# for i in range(0,N-2) #뒤에서 두번째 까지의 공간만 찾으면됨

# cards = list(map(int, input().split()))  # 카드들의 리스트를 받음
# card_count = [0]*10  # 카드들이 몇개씩 있는지를 저장할 리스트.
# count = 0  # run, triplet 세어보기
#     for i in range(6):  # 카드개수 저장.
#         card_count[cards[i]] += 1
#     for i in range(8): 
#         if card_count[i] and card_count[i+1] and card_count[i+2]:  # triplet 계산
#             card_count[i] -= 1
#             card_count[i+1] -= 1
#             card_count[i+2] -= 1
#             count += 1
#         elif card_count[i] == 3:  # run 계산
#             card_count[i] -= 3
#             count += 1
#     if count == 2:
#         print('Baby-Gin')
#     else:
#         print('No')
 
# return(cards)

cards = list(map(int, input().split())) 

card_counts = [0] * 10  # 10 개짜리 틀을 만들어 주고
cnt = 0 #런과 트리플릿의 숫자를 담는

for num in range(6): #6자리 비교  
    card_counts[num] += 1  # 뽑아져 나올 때마다 

answer = False

for card_num in cnt:
    if card_num >= 3:
        answer = True
        break

print(cards)