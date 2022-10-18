#런(run) : 연속된 숫자 3개
#트리플릿(triplet) : 동일한 숫자 3개
# 6자리 숫자를 입력함
#중복을 포함해 6자리로 만들 수 있는 모든 경우의 수를 나열
cards = int(input())
card_list = []
cnt = [0] * 12  # 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트

for i in range(6): #뽑은 6장 비교
    card_list.append(cards % 10)  #나머지를 리스트에 담아 리스트 형성
    cards = cards // 10

    i = 0                                  #비교할 초기값 설정
    triplet = run = 0                      #0으로 초기화 두개를 더해서 2가 되면 babygin
    while i < 10 :
        if cnt[i] >= 3:                    #triplet을 먼저 조사하고 반복할 때 다시 초기화
            cnt[i] -= 3                    #triplet가 발견되면 빼고
            triplet += 1                   # 한개 추가
            continue;            #triplet을 찾게 되면 다시 while로 돌아가서 triplet과 run을 다시 찾음, 없다면 다음으로
        if cnt[i] >= 1 and cnt[i+1] >= 1 and cnt[i+2] >= 1:  #run 조사 후 데이터 초기화
            cnt[i] -= 1                    #3자리가 모두 같다면 run
            cnt[i+1] -= 1
            cnt[i+2] -= 1
            run += 1
            continue
        i += 1
    if run + triplet == 2:
        print('baby gin')
    else:
        print('lose')