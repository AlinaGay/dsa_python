new_tuple = ('a','b','c','d','e')

print('f' in new_tuple) # TC = O(n), false because 'f' is not in new_tuple
#print(new_tuple.index('f')) # TC = O(n), error because 'f' is not in new_tuple

def searchTuple(p_tuple, element):
  for i in range(0,len(p_tuple)):
    if p_tuple[i] == element:
      return f'The {element} is found at {i} index'
  return 'The element is not found'  

print(searchTuple(new_tuple, 'a'))