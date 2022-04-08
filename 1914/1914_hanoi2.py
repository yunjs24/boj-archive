N = int(input())
ans = []
 
def hanoi(num, src, tmp, dst):
  if num == 1:
    print(src, dst)
  else:
    hanoi(num-1, src, dst, tmp)
    hanoi(num-1, tmp, src, dst)    
 
if N <= 20:
  print(2 ** N - 1)
  hanoi(N, 1, 2, 3)
elif N > 20:
  print(2 ** N - 1)
 