'''
5
1 - 2 3
2 - 4 5
3 10
4 88
5 65

'''

def post_order(v):
    #연산자에 따라서
    #왼쪽자식 괄과 - 오른쪽자식 결과
    if value[v] not in '+-*/':
        return value[v]
    else:
        l_result = float(post_order(left[v]))
        r_reuslt = float(post_order(right[v]))
        return l_result - r_reuslt

T = 10
for tc in range(1, T+1):
    N = int(input())
    left = [0]*(N+1)  # 왼쪽자식 정보를 저장할 배열
    right = [0]*(N+1) # 오른쪽 자식정보를 저장할 배열
    value = [None]*(N+1)              #값(또는 연산자)을 저장할 배열
    for i in range(N):
        data = input()
        if len(data) == 2:  # 자식이 없는 경우, 단말 노드, 피연산자
            value[int(data[0])] = data[1]
        else: #자식이 있는 경우, 연산자
            value[int(data[0])] = data[1]
            left[int(data[0])] = int(data[2])
            right[int(data[0])] = int(data[3])

    # 후위 순회 하면서 계산하기기
    result = post_order(1)
    print(f'#{tc} {result}')

