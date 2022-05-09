import sys
readline = sys.stdin.readline
from collections import deque
T = int(readline())
g = []
vectors = [(1,2),(2,1),(1,-2),(2,-1),(-2,1),(-1,2),(-2,-1),(-1,-2)]
def bfs():
    q = deque()

    l = int(readline())
    g = [[0 for _ in range(l)] for _ in range(l)]
    
    y,x = map(int,readline().split())
    now = (x,y)
    g[x][y] = 1

    y,x = map(int,readline().split())
    dest = (x,y)
    
    q.append(now)

    while q:
        vertex = q.popleft()
        x,y = vertex
       

        for v in vectors:
            dx, dy = v
            next_x = x + dx 
            next_y = y + dy
            
            if next_x < 0 or next_x >= l or next_y < 0 or next_y >= l:
                continue
            if g[next_x][next_y] == 0:
                
                if (next_x,next_y) == dest:
                    return g[x][y]

                g[next_x][next_y] = g[x][y] + 1
                q.append((next_x,next_y))
    return 0

for _ in range(T):
    print(bfs())