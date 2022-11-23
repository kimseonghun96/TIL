import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input()))
    # print(num)
    one = []*N
    # print(one)

    max_cnt = 0

    for i in range(len(num)):
        if num[i] == 1:
            one.append(num[i]) # 1을 담다가 0을 만나면 cnt 에 len(one)을 담고 다시

            # print(one)

        elif num[i] == 0 :
            if max_cnt < len(one):
                max_cnt = len(one)
            # print(num)
            one = []      # 초기화

    #위에서 초기화 안된게 남아있음 확인하기
    # print(one)
    if max_cnt < len ( one ):
        max_cnt = len ( one )



    print(f'#{tc} {max_cnt}')

    #     print(num[0])
    #     if num[i] == 1 :
    #         stack.append(1)
    # print(stack)

# N = int(input())