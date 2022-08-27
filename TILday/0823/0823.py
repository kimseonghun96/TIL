'''
# 그냥 조합 2개뽑기
arr = ['A', 'B', 'C']
for i in range(2):
    for j in range(i+1, 3):
        print(arr[i], arr[j])

# A B
# A C
# B C

# 중복조합 2개뽑기
arr = ['A', 'B', 'C']
for i in range(3):
    for j in range(i, 3):
        print(arr[i], arr[j])

# A A
# A B
# A C
# B B
# B C
# C C
'''

# 재귀 조합
arr = ['A', 'B', 'C', 'D', 'E']
sel = [0, 0, 0]


def combination(idx, sidx):
    if sidx == 3:  # sel 길이 범위를 벗어나면 sel이 확정됐다는 소리니까 print
        print(sel)
        return

    if idx == 5:  # 얘도 벗어나지 않아야 함
        return

# 위의 두개 자리 바뀌면 안됨ㅎ

    sel[sidx] = arr[idx]  # sidx가 가리키는 위치에 idx가 가리키는 재료를 넣음
    combination(idx+1, sidx+1)  # 첫번째로는 두개의 화살표가 동시에 오른쪽으로 가보고
    combination(idx+1, sidx)  # 두번째로는 arr 쪽 화살표만 혼자 가봄.


combination(0, 0)

print('--------------')

# 좀 더 일반화된 버전
# arr2 = ['A', 'B', 'C', 'D', 'E']
# sel2 = [0, 0, 0]
#
# def combi_rep(idx, sidx):
#     if sidx == m:
#         print(*sel)
#         return
#
#     if idx == n:
#         return
#
#     sel[sidx] = arr[idx]
#     combi_rep(idx, sidx+1)
#     combi_rep(idx+1, sidx)
#
#
# n, m = map(int, input().split())
# arr2 = list(range(1, n+1))
# sel2 = [0]*m
# combi_rep(0, 0)