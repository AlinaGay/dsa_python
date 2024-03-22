import numpy as np

custom_arr = np.array([1,2,3,4,5])
print(custom_arr)

def linearSearch(arr, target):
  for i in range(len(arr)):
    if arr[i] == target:
      return i
  return "No such element"

print(linearSearch(custom_arr, 0))
print(linearSearch(custom_arr, 3))