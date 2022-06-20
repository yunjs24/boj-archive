import sys

N, M= map(int,sys.stdin.readline().split())

cards = list(map(int, sys.stdin.readline().rstrip().split()))

def getCloserM(N, M, cards):
    max = 0
    for i in range(N-2): #0 ~ 0
        for j in range(i+1,N-1):         
            for k in range(j+1,N):
                sum = cards[i] + cards[j] + cards[k]
                if sum == M:
                    return sum
                elif max < sum < M:
                    max = sum
    
    return max
print(getCloserM(N,M, cards))

