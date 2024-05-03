myDict = {'name':'Alina', 'age': 37, 'address': 'Serbia', 'degree':'specialist'}

another_dict = myDict.copy()
print(another_dict)
print('-------------------------------')

new_dict = {}.fromkeys([1,2,3],0)
print(new_dict)
print('-------------------------------')

print(myDict.get('age', 27))
print(myDict)
print('-------------------------------')

myDict.clear()
print(myDict)