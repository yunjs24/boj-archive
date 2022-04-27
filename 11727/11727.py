n=int(input())
ans = [0]*1001

def solution(n):
    if n==1:
        return 1
    if n==2:
        return 3
    if ans[n]:
        return ans[n]
    prev = 2*solution(n-2)
    next = solution(n-1)
    ans[n] = prev + next
    return ans[n]

print(solution(n)%10007)