readline = __import__('sys').stdin.readline

N, M = map(int, readline().split())
nums = list(map(int, readline().split()))
dp = [0] * len(nums)
dp[0] = nums[0]

for i in range(1, len(nums)):
    dp[i] = dp[i-1] + nums[i]

for _ in range(0, M):
    i, j = map(int, readline().split())
    if i==1:
        print(dp[j-1])
    else:
        print(dp[j-1] - dp[i-2])