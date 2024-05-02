myDict = {'name':'Alina', 'age': 37, 'address': 'Serbia', 'degree':'specialist'}

del myDict['age']
print(myDict)
print('-------------------------------------')

removed_element = myDict.pop('name')
print(myDict)
print('-------------------------------------')

removed_element = myDict.popitem()
print(myDict)