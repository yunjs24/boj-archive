
n = int(input())
arr  = list(map(int, input().split()))

ohken = [-1] * n
stack = []

for i in range(n):
    while stack and (stack[-1][0] < arr[i]):
        tmp, idx = stack.pop()
        ohken[idx] = arr[i]
    stack.append([arr[i], i])

print(*ohken)