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

#7 remove last array element usin pop() method
print("------------------------------------")
arr_1.pop()
print(arr_1)