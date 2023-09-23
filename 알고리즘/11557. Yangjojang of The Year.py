# 학교랑 소비 금액 받고
# 소비금액 중에 제일 큰거 찾아서
# 가장큰 소비금액을 가지고 있는 학교 출력


T = int(input())

for tc in range(T):
    ans = []
    for i in range(int(input())):
        school = input().split()
        school[1] = int(school[1])
        ans.append(school)
    num = []
    for j in range(len(ans)):
        num.append(ans[j][1])

    for k in range(len(ans)):
        if max(num) == ans[k][1]:
            print(ans[k][0])

