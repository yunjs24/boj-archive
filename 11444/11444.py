readline = __import__('sys').stdin.readline
import math
n=int(readline())
d = [0]*41
def fibo(n):
    sqrt_5 = math.sqrt(5)
    ans = 1 / sqrt_5 * ( ((1 + sqrt_5) / 2) ** n  - ((1 - sqrt_5) / 2) ** n )%1000000007
    return int(ans)

print(fibo(n))