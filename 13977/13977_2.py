import sys
readline = sys.stdin.readline
p=int(1e9)+7
factorial = [1] * (4000001)
for i in range(1,4000001):
    factorial[i] = i*factorial[i-1]%p

def power_mod(x,n): # return x**n 
    if n == 1:
        return x % p
    if n & 1:
        return power_mod(x, n) % p
    return power_mod(x * x % p, n // 2) % p

M = int(readline())
for _ in range(M):
    n, k = map(int, input().split())
    print(factorial[n] * power_mod() % p)
