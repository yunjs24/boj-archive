readline = __import__('sys').stdin.readline

N = int(readline())
info = []
for _ in range(N):
  info.append(list(map(int, readline().split())))

info.sort(key = lambda x: (x[1], x[0]))

cnt = 1
t_end = info[0][1]
for i in range(1,N):
  if info[i][0] >= t_end:
    cnt += 1
    t_end = info[i][1]

print(cnt)