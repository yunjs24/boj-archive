# N과 M(8)

readline = __import__('sys').stdin.readline
N, M = map(int, input().split())
numbers = list(map(int, readline().split()))
numbers.sort()
case = []
ans = []
def solution(array,r):
    global ans
    if r==0:
        ans.append(list(case))
        return
    else:
        for i in range(len(array)):
            case.append(array[i])
            solution(array[i:],r-1)
            case.pop()

solution(numbers,M)

for r in ans:
    print(*r)