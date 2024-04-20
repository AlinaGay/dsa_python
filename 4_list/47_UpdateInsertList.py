myList = [1,2,3,4,5,6,7]
print(myList)
print("------------------------------------------")

myList[2] = 33
print(myList)
print("------------------------------------------")

myList.insert(0,11)
print(myList)
print("------------------------------------------")

newList = [12,13,14]
myList.extend(newList)
print(myList)
print("------------------------------------------")

myList.append(55)
print(myList)