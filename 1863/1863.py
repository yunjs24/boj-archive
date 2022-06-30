readline = __import__('sys').stdin.readline

n = int(readline().rstrip())

stack = []
answer = 0

for _ in range(n):
	x,y = map(int,readline().rstrip().split())
	l = len(stack)
	while l > 0 and stack[-1] > y:
		answer += 1
		stack.pop()
	if l > 0 and stack[-1] == y:
		continue
	stack.append(y)

while len(stack) > 0:
	if stack[-1] > 0:
		answer += 1
	stack.pop()

print(answer)