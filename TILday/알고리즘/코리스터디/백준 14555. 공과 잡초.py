'''
3
||||||
(|..|)
.|.(|...||)|...()..
'''
# 완전한 공과 공이 가려진 경우를
# 다 +1 해줌

T = int(input())
for tc in range(1, T+1):
    weed = list(input())
    ans = 0
    for i in range(len(weed)-1):
        if weed[i] == '(' and weed[i+1] == '|':
            ans += 1
        if weed[i] == '|' and weed[i+1] == ')':
            ans += 1
        if weed[i] == '(' and weed[i+1] == ')':
            ans += 1
    print(f'#{tc} {ans}')
