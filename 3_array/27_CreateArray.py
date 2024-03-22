# array model
import array

array_1 = array.array('i') # empty array, a minimal contiguous block of memory is allocated for the array elements as there are no elements to store.
print(array_1)

array_2 = array.array('i', [1,2,3,4])# ----------- TC = O(n), SC = O(n)
print(array_2)

# Now one of the advantages of array model is that 
# it is more memory efficient than the list for storing 
#the large types of the same data type.
# And it is a Python standard library.
# No additional installation is required for this.

# Now the only limitation is that it supports 
# only basic data types. So you cannot create 
# an array by using the array model with 
# the custom data types or mixed data types. 
# So the arrays that are created by using 
# the array model is going to be homogeneous, 
# which means that we will have only same data type over here.


# NumPy model 
import numpy as np

array_3 = np.array([], dtype = int)
print(array_3)
array_4 = np.array([5,6,7,8]) # ----------- TC = O(n), SC = O(n)
print(array_4)

# By using the numpy module we can create a three dimensional array.
# Now the advantage of numpy module is that it provides a feature 
# rich and high performance array object, and it is supporting 
# the wide range of numerical operations and functions.
# Now disadvantage is that it is not part of the Python 
#standard library, so you have to install additional library to be able to use it.
