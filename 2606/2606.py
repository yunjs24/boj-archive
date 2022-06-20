readline = __import__("sys").stdin.readline

def dfs(start):
    visit = []
    stack = [start]
    
    while stack:
        v = stack.pop()
        if v not in visit:
            visit.append(v)
            stack.extend(g[v])
    return len(visit)-1

n = int(readline())
g = [[] for _ in range(n + 1)]
link = int(readline())

for _ in range(link):
    i,j = map(int,readline().split())
    g[i].append(j)
    g[j].append(i)

print(dfs(1))