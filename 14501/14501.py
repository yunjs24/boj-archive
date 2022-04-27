import sys

ans = []

N = int(input())
T = list()
P = list()
for i in range(N):
    t, p = map(int, sys.stdin.readline().split())
    T.append(t)
    P.append(p)

def getPayCase(T,P,d, sum): # day : 0 ~
    global ans, N
    if  d >= N:
        ans.append(sum)
        return
    elif d + T[d] > N:
        ans.append(sum)
        getPayCase(T,P,d+1,sum)
    else :
        for now in range(d,N):
            if now + T[now] <= N:
                getPayCase(T,P,now+T[now],sum+P[now])
            next = now + 1
            if next < N and next + T[next] <= N:
                getPayCase(T,P,next+T[next],sum+P[next])

getPayCase(T,P,0, 0)
print(max(ans))


