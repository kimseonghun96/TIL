p = 1 #처음 줄 설 사람 번호

q = []
N = 20000       # 나눠준 마이쮸 갯수
m = 0
v = 0

while m<N:
    # input()
    q.append((p, 1, 0)) #처음 줄서는 사람, 몇개를 받아가는지, 나눠준 사탕 수
    # print(q)
    v, c, my = q.pop(0)
    # print(f'q에 있는 사람 수 {len(q)+1}, 받아갈 사탕 수{c}, 나눠 준 사탕 수{m}')
    m += c
    q.append((v, c+1, my+c)) # 마이쮸를 받고 다시 서는 사람
    p += 1
print(f'마지막 받은 사람 : {v}')