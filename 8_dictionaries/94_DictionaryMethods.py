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

print(myDict.get('city'))
print('-------------------------------')

print(myDict.items())
print('-------------------------------')

print(myDict.keys())
print('-------------------------------')

print(myDict.values())
print('-------------------------------')

print(myDict.popitem())
print(myDict)
print('-------------------------------')

print(myDict.setdefault('name','added'))
print(myDict)
print('-------------------------------')

print(myDict.setdefault('name1','added'))
print(myDict)
print('-------------------------------')

print(myDict.pop('name2','not'))
print(myDict)
print('-------------------------------')

print(myDict.pop('name1','not'))
print(myDict)
print('-------------------------------')

new_dict = {'a':1, 'b':2, 'c':3}
print(myDict.update(new_dict))
print(myDict)
print('-------------------------------')

myDict.clear()
print(myDict)