readline = __import__('sys').stdin.readline

triangle = []

n = int(readline())

for _ in range(n):
    triangle.append(list(map(int, readline().split())))

for i in range(1,n):
    triangle[i][0] += triangle[i-1][0]
    triangle[i][i] += triangle[i-1][i-1]
    for j in range(1,len(triangle[i])-1):
        triangle[i][j] += max(triangle[i-1][j-1],triangle[i-1][j])

print(max(triangle[n-1]))