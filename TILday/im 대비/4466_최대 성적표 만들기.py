import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    # print(N)
    max_score = list(map(int, input().split()))
    # print(max_score)
    max_score.sort()
    max_score.sort(reverse=True)
    # print(max_score)
    print(f'#{tc }', sum(max_score[:K]))


