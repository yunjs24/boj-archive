from sys import stdin, stdout

factorial = [1] * 4000001
for idx in range(2, 4000001):
    factorial[idx] = (factorial[idx-1] * idx) % 1000000007

def pow(n, k):
    if k == 1:
        return n
    pow_half = pow(n, k//2)
    if k % 2 == 0:
        return (pow_half ** 2) % 1000000007
    else:
        return (pow_half ** 2 * n) % 1000000007

def inverse(n):
    return pow(factorial[n], 1000000005)

m = int(input())
for _ in range(m):
    n, k = map(int, stdin.readline().split())
    stdout.write(str((factorial[n] * inverse(n-k) * inverse(k)) % 1000000007))
    stdout.write('\n')
stdout.flush()