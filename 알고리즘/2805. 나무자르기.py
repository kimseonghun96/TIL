n, m = map(int, input().split())

trees = list(map(int, input().split()))

def serch(m, trees):
    start, end = 0, max(trees)
    while start <= end:
        ans = 0
        mid = (start + end) // 2
        for i in trees:
            if i > mid:
                ans += i - mid

        if ans >= m:
            start = mid + 1
        else:
            end = mid - 1

    return end


print(serch(m, trees))