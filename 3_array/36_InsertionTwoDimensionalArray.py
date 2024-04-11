import numpy as np

twoDArray_1 = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoDArray_1)
print("-----------------------------------")

twoDArray_2 = np.insert(twoDArray_1, 0, [[1,2,3,4]], axis = 1) # add column
print(twoDArray_2)
print("-----------------------------------")

twoDArray_3 = np.insert(twoDArray_2, 0, [[1,2,3,4,5]], axis = 0) # add row
print(twoDArray_3)