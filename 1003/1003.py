readline = __import__('sys').stdin.readline
T=int(readline())
d = [0]*41
def fibo(n):
    sqrt_5 = 5 ** (1/2)
    ans = 1 / sqrt_5 * ( ((1 + sqrt_5) / 2) ** n  - ((1 - sqrt_5) / 2) ** n )
    return int(ans)
for _ in range(T):
    n = int(readline())
    if(n == 0):
        print(1,0)
        continue
    if(n == 1):
        print(0,1)
        continue
    if d[n-1] and d[n]:
        print(d[n-1],d[n])
        continue
    else:
        d[n-1],d[n] = fibo(n-1),fibo(n)
        print(fibo(n-1),fibo(n))