'''
2
5 3
2 5 3
7 2
4 6
'''

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())    # N은 학생 수, K는 제출한 사람의 수
    student = list(map(int, input().split()))

    x_student = [1]*(N+1)    # 일단 모두 문제 안풀었다고 가정, 앞에 한칸 추가해줌 1부터 체크하기 위해

    for i in student:        # 문제 푼 놈들은
        x_student[i] = 0     # 문제 안푼놈들 중에서 제외

    ans = []
    for i in range(1, len(x_student)):  # 맨앞칸 제외 첫번째 인덱스 부터 1이면 ans에 추가
        if x_student[i] == 1:
            ans.append(i)

    print(f'#{tc}', *ans)
