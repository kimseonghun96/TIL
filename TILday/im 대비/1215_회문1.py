import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 문자열을 모두 리스트 형태로 매트릭스에 저장
    text_matrix = [list(input()) for _ in range(N)]

    # 매트릭스를 가로로 돌면서, 길이가 M인 문자열을 모두 찾아 회문인지 확인
    for i in range(N):
        for j in range(N-M+1):
            # 인덱스 오류를 피하기 위해, j가 0일 때와 아닐 때를 나눔
            if j == 0:
                if text_matrix[i][j:j + M] == text_matrix[i][j + M - 1::-1]:
                    # 리스트 형태를 문자열 형태로 전환
                    result = ''.join(text_matrix[i][j:j+M])
            else:
                if text_matrix[i][j:j+M] == text_matrix[i][j+M-1:j-1:-1]:
                    result = ''.join(text_matrix[i][j:j+M])

    # 세로로 찾기 위해 매트릭스 전치
    text_matrix = list(zip(*text_matrix))

    # 전치된 매트릭스를 가로로 돌면서, 길이가 M인 문자열을 모두 찾아 회문인지 확인
    for i in range(N):
        for j in range(N-M+1):
            if j == 0:
                if text_matrix[i][j:j + M] == text_matrix[i][j + M - 1::-1]:
                    result = ''.join(text_matrix[i][j:j+M])
            else:
                if text_matrix[i][j:j+M] == text_matrix[i][j+M-1:j-1:-1]:
                    result = ''.join(text_matrix[i][j:j+M])

    print(f'#{tc} {result}')
