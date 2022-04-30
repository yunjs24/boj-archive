import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**6)
T = int(readline())
g = []
vectors = [(-1,0),(1,0),(0,1),(0,-1)]
def dfs(i,j,s=0):
    global M,N
    if i < 0 or i >= N or j < 0 or j >= M:
        return 0
    if g[i][j] == 1:
        g[i][j] = 0
        for v in vectors:
            dx, dy = v
            dfs(i+dx,j+dy)
        return s+1    
    return 0

for _ in range(T):
    M, N, K = map(int,readline().split())
    g = [[0 for _ in range(M)] for _ in range(N)]  
    for i in range(K):
        y, x = map(int,readline().split())
        g[x][y] = 1

    ans = 0
    for i in range(N):
        for j in range(M):
            if dfs(i,j) == 1:
                ans += 1

    print(ans)

    

