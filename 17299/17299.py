readline = __import__('sys').stdin.readline

n = int(readline())
nums = list(map(int, readline().split()))
nums_count = __import__('collections').Counter(nums)
result = [-1] * n
stack = [0]

for i in range(1, n):
    while stack and nums_count[nums[stack[-1]]] < nums_count[nums[i]]:
            result[stack.pop()] = nums[i]
    stack.append(i)

print(*result)