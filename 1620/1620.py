import sys
readline = sys.stdin.readline

N, M = map(int,readline().rstrip().split())
ans = []
dict = {}
inv_dict = {}
for i in range(1,N+1):
    name = readline().rstrip()
    dict[name] = i
    inv_dict[i] = name
for _ in range(M):
    quiz = readline().rstrip()
    if quiz[0].isdigit():
        ans.append(inv_dict[int(quiz)])
    else:#{name: num }
        ans.append(str(dict[quiz]))

print('\n'.join(ans))