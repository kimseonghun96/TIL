N = 10

arr = [[0]*N for _ in range(N)]
dr = [-1,-1,-1, 0, 1, 1, 1, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1]

r, c = 3, 4

#   원하는 거리(칸수)만큼 가고 싶다.
k = 4       # 기준점을 포함해서
for i in range(8):
    for j in range(1, k+1):
        nr = r
