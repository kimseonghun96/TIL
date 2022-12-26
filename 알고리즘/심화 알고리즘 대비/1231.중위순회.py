'''
1 W 2 3
2 F 4 5
3 R 6 7
4 O 8
5 T
6 A
7 E
8 S
'''
def inorder(n):                     # 중위순회
    global answer                   # global 밖의 변수를 함수안에서 만지고 싶을 때
    if n != 0:                      # 0은 안씀 1부터 시작함
        inorder(left[n])
        answer += edges_list[n]
        inorder(right[n])


T = int(10)
for tc in range(1, T+1):
    V = int(input())
    edges_list = ['']*(V+1)                     # str담을꺼
    left = [0]*(V+1)
    right = [0]*(V+1)
    answer = ''
    for _ in range(V):
        edges = list(map(str, input().split()))     # for문 안에서  edges를 만지기 위해
        if len(edges) == 4:                         # 각 케이스마다 노드 연결
            left[int(edges[0])] = int(edges[2])     # str로 받았기 때문에 int로 변경
            right[int(edges[0])] = int(edges[3])
            edges_list[int(edges[0])] = edges[1]
        elif len(edges) == 3:
            left[int(edges[0])] = int(edges[2])     # right 없음
            edges_list[int(edges[0])] = edges[1]
        else:
            edges_list[int(edges[0])] = edges[1]

    inorder(1)              # 정점은 1
    print(f'#{tc} {answer}')



