import math
primes = {} #dict

def primeUpdate(n):
    sieve = [True] * n

    m = int(math.sqrt(n))
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i<<1, n, i):
                sieve[j] = False
    
    #list에서 dict로
    for i in [i for i in range(2, n) if sieve[i] == True]:
        if i in primes.keys():
            primes[i] += 1
        else:
            primes[i] = 1

def solution(N):
    ans = 0
    for i in primes:
        if i > N/2:
            return ans
        diff = N - i
        if diff in primes.keys():
            ans += 1
    return ans


primeUpdate(1000000)

T = int(input())

for _ in range(T):  
    N = int(input())
    print(solution(N))