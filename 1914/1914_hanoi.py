N = int(input())
ans = []
 
def hanoi(num, src, tmp, dst):
  if num == 1:
    ans.append((src, dst))
  else:
    hanoi(num-1, src, dst, tmp)
    ans.append((src, dst))
    hanoi(num-1, tmp, src, dst)    
 
if N <= 20:
  hanoi(N, 1, 2, 3)
elif N > 20:
  answer = 2 ** N - 1
  print(answer)
 
if N <= 20:
  length = len(ans)
  print(length)
  for i in range(length):
    print(ans[i][0], ans[i][1])