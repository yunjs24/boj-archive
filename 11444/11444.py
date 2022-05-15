# readline = __import__('sys').stdin.readline
# import math
# n=int(readline())
# d = [0]*41
# def fibo(n):
#     sqrt_5 = math.sqrt(5)
#     ans = 1 / sqrt_5 * ( ((1 + sqrt_5) / 2) ** n  - ((1 - sqrt_5) / 2) ** n )%1000000007
#     return int(ans)

# print(fibo(n))


def mul(A, B):
    n = len(A)
    Z = [[0]*n for _ in range(n)]
    
    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += A[row][i] * B[i][col]
            Z[row][col] = e % p
            
    return Z

def square(A, k):
    if k == 1:
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= p
        return A
    
    tmp = square(A, k//2)
    if k % 2:
        return mul(mul(tmp, tmp), A)
    else:
        return mul(tmp, tmp)
    
fib_matrix = [[1, 1], [1, 0]]
print(square(fib_matrix, n)[0][1])