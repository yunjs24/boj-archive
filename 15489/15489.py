readline = __import__('sys').stdin.readline
R, C, W = map(int, readline().split())

factorial = [1]

def comb(n,k):
    return factorial[n]//(factorial[n-k]*factorial[k])

for i in range(1,R+W):
    factorial.append(factorial[i-1]*i)

if W==1:
    print(comb(R-1,C-1))
    exit()
ans = 0
for i in range(W):
    #print(R+W-1,C+i)
    #print(R-1+i,C+i)
    ans = ans + comb(R+W-1,C+i) - comb(R-1+i,C+i)
print(ans)
