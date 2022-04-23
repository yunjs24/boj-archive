import sys
readline = sys.stdin.readline
p=int(1e9)+7
factorial = [1] * (4000001)
for i in range(1,4000001):
    factorial[i] = i*factorial[i-1]%p

def power_mod(x,n): # return x**n 
    if n==1:
        return x % p
    if n&1:
        return power_mod(x, n-1) * x % p
    return power_mod(x*x%p,n//2)%p

def update(s,n,fact):
    for i in range(s,n):
        fact[i] = i*fact[i-1]%p


# top = 1000000


M = int(readline())
for _ in range(M):
    n,k = map(int,input().split())
    # if n > top:
    #     update(top,n+1,fact)
    #     top = n
    # print("power_mod:",power_mod(fact[n-k] * fact[k]%p,p-2))
    print(factorial[n] * power_mod((factorial[n-k] * factorial[k]) % p, p-2) % p)
