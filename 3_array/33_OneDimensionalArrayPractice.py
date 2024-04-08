from array import *

#5 extend array
arr_1 = array("i", [1,2,3,4,5,6])
arr_2 = array('i', [8,9,0])
arr_1.extend(arr_2)

print(arr_1)

#6 add items from list into array using fromList() method
print("------------------------------------")
tempList = [20,30,40]
arr_1.fromlist(tempList)
print(arr_1)

#7 remove any array element using remove() method
print("------------------------------------")
arr_1.remove(20)
print(arr_1)

#8 remove last array element usin pop() method
print("------------------------------------")
arr_1.pop()
print(arr_1)

#9 fetch any element through its index using index() method
print("------------------------------------")
print(arr_1.index(30))

#10 reverse a python array using everse() method
print("------------------------------------")
arr_1.reverse()
print(arr_1)

#11 get array buffer information through buffer_info() method
print("------------------------------------")
print(arr_1.buffer_info())

#12 check for number of occurances of an element using count() method
print("------------------------------------")
print(arr_1.count(11))

#13 convert array to string using tobytes() method
print("------------------------------------")
strTemp = arr_1.tobytes()
print(strTemp)

#14 append a string to char rray using fromstring() method
print("------------------------------------")
ints = array('i')
ints.frombytes(strTemp)
print(ints)

#15 convert array to a python list using tolist() method
print("------------------------------------")
print(ints.tolist())

#16 slice lements from an array
print("------------------------------------")
print(arr_1[1:4])