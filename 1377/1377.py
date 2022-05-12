readline = __import__('sys').stdin.readline
N = int(readline())

changed = False
A = []
toPullCount = []
for i in range(N):
    A.append([int(readline()),i])
sorted_A = sorted(A, key = lambda x: x[0])

for i in range(0,N):
    #toPullCount[A[i]] = i - sorted_A.index(A[i]) -> index() : O(n)
    toPullCount.append(A[i][1]-sorted_A[i][1])

ans = -min(toPullCount) + 1
print(ans)