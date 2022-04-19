n = int(input())
s = list(map(int, input().split()))
s.sort()
num = 0
for i in range(n):
    for j in range(i + 1):
        num += s[j]
print(num)