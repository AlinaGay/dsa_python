from array import *

custom_arr = array('i', [4,5,6,7,8])
print(custom_arr)

def accessElement(arr, index):
  if index >= len(arr):
    return "There is no any element with this index"
  else:
    return arr[index]
  
print(accessElement(custom_arr, 3))
print(accessElement(custom_arr, 8))
