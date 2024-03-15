def flatten(arr):
  if not len(arr):
    return []
  if len(arr) == 0:
    return []
  else:
    [].append(flatten(arr[-len(arr)]))

print(flatten([1, 2, 3, [4, 5]]))    

#print(len([1, 2, 3, [4, 5]]))