import numpy as np

twoDArray = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoDArray)

def accessElements(array, rowIndex, colIndex):
  if rowIndex >= len(array) and colIndex >= len(array[0]):
    print("Incorrect index!")
  else:
    print(array[rowIndex][colIndex])  

print("------------------------------------------------------")
accessElements(twoDArray, 1, 2)    
accessElements(twoDArray, 2, 3)   