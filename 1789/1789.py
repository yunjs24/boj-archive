import sys
readline = sys.stdin.readline

s = int(readline())
i = 1
flag = 0
while True:
    flag += i
    i += 1
    if flag > s:
        print(i - 2)
        break

