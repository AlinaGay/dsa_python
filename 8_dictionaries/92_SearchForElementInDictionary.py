myDict = {'name':'Alina', 'age': 37, 'address': 'Serbia'}

def searchDict(dict, value):
  for key in dict:
    if dict[key] == value:
      return key, value
  return "The value does not exist"

print(searchDict(myDict, 37))