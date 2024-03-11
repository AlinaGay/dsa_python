def recursiveMethod(n):
  if n < 1:
    print("n is less than 1")
  else:
    recursiveMethod(n-1) #initially this calls itself more than n times
    print(n) # then it ptints n after doing stack is empty

recursiveMethod(4)     