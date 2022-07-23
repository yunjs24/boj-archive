from collections import deque
m,n = map(int,input().split())
graph = []
queue = deque([])
for i in range(n):
    graph.append(list(map(int,input().split())))
    
    for j in range(m): 
        if graph[i][j]==1:
            queue.append([i,j])
            
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs():
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            n_x = x+dx[i]
            n_y = y+dy[i]
            if 0<=n_x<n and 0<=n_y<m and graph[n_x][n_y]==0:
                queue.append([n_x,n_y])
                graph[n_x][n_y] = graph[x][y]+1
bfs()
answ = 0
for i in graph:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    answ = max(answ,max(i))
print(answ-1)
