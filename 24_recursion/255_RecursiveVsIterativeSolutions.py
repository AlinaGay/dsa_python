def recursivePowerOfTwo(n):
  if n == 0:
    return 1
  else:
    power = recursivePowerOfTwo(n-1)
    return power*2
  

def iterativePowerOfTwo(n):
  i = 0
  power = 1
  while i < n:
    power = power*2
    i = i + 1
  return power    


print(recursivePowerOfTwo(3))