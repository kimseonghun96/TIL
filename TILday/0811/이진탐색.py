T=int(input())
for tc in range(T):
    N = int(input())
    # num_sort=map(int, input().split())
    for num in range(N):
        num_sort = [i]
        if num_sort[i] < num:
            num_sort[i], num_sort[j] = num_sort[j], num_sort[i]


