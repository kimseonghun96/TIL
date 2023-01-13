#영수의 모든 답과 일치하는 숫자만 True 값으로 둔다.

import sys

N = int(input())
cnt = [True] * 999
#False로 두면 값 구하기가 어려워진다..True로 두고 False인 것 거르기
ans = 0
for _ in range(N):
    num, s, b = map(int, sys.stdin.readline().split())
    num = str(num)

    for i in range(123, 988):
        i = str(i)
        #1 ~ 9에서 서로 다른 3가지 수를 구하는 것이므로, 아닌 것은 False로 걸러준다.
        if i[0] == "0" or i[1] == "0" or i[2] == "0":
            cnt[int(i)] = False
        if i[0] == i[1] or i[1] == i[2] or i[0] == i[2]:
            cnt[int(i)] = False
        s_cnt = 0
        b_cnt = 0
        for j in range(3):
            for k in range(3):
                if i[j] == num[k]:
                    if j == k:
                        s_cnt += 1
                    else:
                        b_cnt += 1

        if cnt[int(i)] and s_cnt == s and b_cnt == b:
            cnt[int(i)] = True
        else:
            cnt[int(i)] = False

for i in range(123, 988):
    if cnt[i]:
        ans += 1

print(ans)