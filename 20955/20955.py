from collections import deque

input = __import__('sys').stdin.readline
n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
visit = [0] * (n + 1)
for i in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
ans = -1
edge = 0
for i in range(1, n+1):
    if not visit[i]:
        ans += 1
        visit[i] = 1
        q = deque([i])
        while q:
            x = q.popleft()
            for nx in g[x]:
                if not visit[nx]:
                    visit[nx] = 1
                    q.append(nx)
                    edge += 1
print(ans + m - edge)
cs