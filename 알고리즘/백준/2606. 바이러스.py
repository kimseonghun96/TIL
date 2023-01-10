#인접리스트
N = int(input())
arr = [[0] * (N+1) for _ in range(N+1)]
for i in range(int(input())):
    n, m = map(int, input().split())
    arr[n][m] += 1
    arr[m][n] += 1

visited = []
stack = [1]

while stack:
    virus = stack.pop()
    if virus not in visited:
        visited.append(virus)

    for destination in range(N+1):
        if arr[virus][destination] and destination not in visited:
            stack.append(destination)

print(len(visited)-1) #1은 제외