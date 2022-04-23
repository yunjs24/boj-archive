readline = __import__('sys').stdin.readline

T = int(readline())

def botup(table,n):

    d = [[0]*100001] + [[0]*100001]

    for i in range(1,n+1):
        d[0][i] = table[0][i] + max(d[1][i-1],
                                    d[1][i-2])
        d[1][i] = table[1][i] + max(d[0][i-1],
                                    d[0][i-2])
    return max(d[0][n],d[1][n])

for _ in range(T):
    n = int(readline())
    table = [[0]+list(map(int,readline().split())) for i in range(2)]
    print(botup(table, n))
    