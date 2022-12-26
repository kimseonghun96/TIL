def bfs(w, s):
    global w, s
    arr[r][c] = 1




r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
visit = [[0]*c for _ in range(r)]
wolf = 0
sheep = 0