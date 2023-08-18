arr = list(input())
stack = []
ans = 0

for i in range(len(arr)):
    if arr[i] == '(':
        stack.append(arr[i])
    elif arr[i] == ')':
        if arr[i-1] == '(':
            stack.pop()
            ans += len(stack)
        elif arr[i-1] == ')':
            stack.pop()
            ans += 1


print(ans)