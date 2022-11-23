'''
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1
'''

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    idx_arr = []                # 배열의 인덱스를 저장 해줌  맨 왼쪽이 0이라고 했으니까 그대로
    for i in range(N):
        idx_arr.append(i)

    idx_arr[M] = 999             # 내가 찾아야 할 곳의 인덱스의 값을 따로 지정해 줌

    # print(idx_arr)
    ans = 0
    while arr:                          # 배열을 돌거임
        if arr[0] == max(arr):          # 맨앞의 값이 그 배열에서 가장 큰 값일 때 작동
            ans += 1                    # 조건을 충족했다면 내가 찾아야 되는 값이 맨앞으로 올때까지 카운트
            if idx_arr[0] == 999:        # 찾으면 출력하고 멈추기
                print(ans)
                break
            else:
                arr.pop(0)              # 못 찾으면 맨 앞 하나씩 제거
                idx_arr.pop(0)

        else:                           # 아니라면 배열과 인덱스의 첫번째 값을 맨 뒤로 옮겨줌
            arr.append(arr.pop(0))
            idx_arr.append(idx_arr.pop(0))








