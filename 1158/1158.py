N, K = map(int, input().split())
answer = []
arr = list(range(1,N+1))
remember = 0
for i in range(N):
    remember += K-1
    while remember > len(arr)-1:
        remember = remember - len(arr)
    answer.append(arr.pop(remember))

print('<'+', '.join(map(str, answer))+'>')
