myList = ['a','b','c','d','e']
myList[0:2] = ['x','y']
print(myList[:])
print('---------------------------------------------')

print(myList.pop(1))
print(myList[:])
print('---------------------------------------------')

del myList[2]
print(myList[:])
print('---------------------------------------------')

del myList[0:1]
print(myList[:])
print('---------------------------------------------')

myList.remove('e')
print(myList[:])