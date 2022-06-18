import sys
sys.setrecursionlimit(10**7)
readline = sys.stdin.readline
map_matrix = list()
vectors = [(1,0),(0,1),(0,-1),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]
def dfs(i,j,s=0):
    global w,h
    if i<0 or i>=h or j<0 or j>=w:
        return 0
    if map_matrix[i][j] == 1:
        map_matrix[i][j] = 0
        for v in vectors:
            dx, dy = v
            dfs(i+dx,j+dy)
        return s+1
    return 0
    
while True:
    w,h = map(int, readline().split())
    if w==0 and h==0:
        break
    
    map_matrix = []
    
    for _ in range(h):
        map_matrix.append(list(map(int, readline().split())))

    cnt = 0
    for i in range(h):
        for j in range(w):
            if dfs(i,j)==1:
                cnt += 1
    print(cnt)


