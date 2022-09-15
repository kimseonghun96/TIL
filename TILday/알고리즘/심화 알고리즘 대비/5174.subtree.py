'''
3
5 1
2 1 2 5 1 6 5 3 6 4
5 1
2 6 6 4 6 5 4 1 5 3
10 5
7 6 7 4 6 9 4 11 9 5 11 8 5 3 5 2 8 1 8 10
'''



def postorder(n):
    global answer
    # 순회할 때마다 + 1
    postorder(left[n])
    postorder(right[n])
    answer += 1


T = int(input())
for tc in range(T, T+1):
    E, N = input().split()
    E = int(E)
    answer = ''
    child_num = list(map(int, input().split()))
    subtree = [0]*(E+2)
    left = [0]*(E+2)
    right = [0]*(E+2)
    for i in range(E+2):
        parent, child = subtree[2*i], subtree[2*i+1]
        if left[parent] == 0:
            left[parent] = child
        else:
            right[parent] = child

postorder(2)
print(answer)