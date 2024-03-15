def recursiveRange(num):
  assert num > 0 and int(num) == num, "The number must be positive integer only!"
  if num == 0:
    return 0
  else:
    return num + recursiveRange(num-1)
    
print(recursiveRange(1.2))    