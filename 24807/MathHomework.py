readline = __import__('sys').stdin.readline
b,c,d,l = map(int, readline().split())
cnt = 0
for i in range(0, int(l / b + 1)):
    for j in range(0, int(l / c + 1)):
        for k in range(0, int(l / d + 1)):
            s = i*b + j*c + k*d
            if s == l:
                print(i,j,k)
                cnt += 1
            elif s > l:
                break

if cnt == 0:
    print("impossible")