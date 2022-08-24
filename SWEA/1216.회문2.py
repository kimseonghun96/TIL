import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    temp = [list(input()) for _ in range(100)]  # 일단 리스트로 된 100x100칸 만들어야 할듯?
    # 가로랑 세로(zip) 리스트로 만들어서 다 보면서 회문을 찾아야댐
    # 회문을 담는 칸을 만들어야 겠지?
    # 그리고 길이가 가장 긴 걸 출력하면 된다
    zip_temp = list(zip(*temp)) #세로 회문 확인을 위한 전치
    answer = 0

    for i in range(100):
        for j in range(100):
            for k in range(j+1, 100):
                if temp[i][j:j+k+1] == temp[i][j:j+k+1][::-1]: #가로 회문 찾고
                    if answer < len(temp[i][j:j+k+1]):
                        answer = len(temp[i][j:j+k+1])

                if zip_temp[i][j:j+k+1] == zip_temp[i][j:j+k+1][::-1]:
                    if answer < len(zip_temp[i][j:j+k+1]):        # 세로 회문 찾았다
                        answer = len(zip_temp[i][j:j+k+1])

    print(f'# {tc} {answer}')
