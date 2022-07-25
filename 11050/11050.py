N, K = map(int, input().split())

numerator = 1
denominator = 1

for i in range(N,N-K,-1):
    numerator *= i

for i in range(K,0,-1):
    denominator *= i

print(numerator//denominator)