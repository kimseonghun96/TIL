T = int(input())
for tc in range(1, T+1):
    result = input()
    # print(result)
    # print(result.count('x'))
    if result.count(('x')) < 8:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')

# 총 15안에서의 결과를 구하면 되기 때문에 input에서 x의 개수가 8이하일 경우엔 YES 아닐 경우 NO