readline = __import__('sys').stdin.readline
n,k = map(int, readline().split())

factorial = [1]
for i in range(1,n+1):
  factorial.append(factorial[i-1]*i)

print(int(factorial[n-1]/(factorial[n-k]*factorial[k-1])))
