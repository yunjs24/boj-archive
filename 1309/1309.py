from sys import stdin
p,n=3,7
for _ in range(1,int(stdin.readline())):n,p=(2*n+p)%9901,n
print(p)
