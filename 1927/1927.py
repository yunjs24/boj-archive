import heapq

readline = __import__('sys').stdin.readline
heap = []

for _ in range(int(readline())):
    num = int(readline())
    if num != 0:
        heapq.heappush(heap, num)
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)