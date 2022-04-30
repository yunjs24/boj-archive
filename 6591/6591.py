readline = __import__('sys').stdin.readline


while True:
    n,k = map(int, readline().split())
    if n == 0 and k == 0:
        break
    if k == 0:
        print(1)
        continue
    if n//2 > k:
        k = n-k
    res = 1
    for i in range(k+1,n+1): # 3 ~4 4 3 
        res *= i
        res //= i-k
    print(res)

